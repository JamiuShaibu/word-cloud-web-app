from datetime import timedelta
from typing import TextIO

from PIL import Image
import streamlit as st
import PyPDF2
import re
import docx


@st.cache_resource(ttl=timedelta(hours=1), show_spinner=False)
def clean_string_content(string_content: str) -> str:
    # Substitute non-word characters followed by a space character with spaces
    string_data = re.sub(r'\W+ ', ' ', string_content)
    # Remove special characters that are found in string.
    string_data = re.sub(r'["“”;,()„]|[\[\]]', '', string_data)
    # Replace the special characters in the re that are found in string with a space.
    string_data = re.sub(r' -| :|: |- |—', ' ', string_data)
    # Remove periods that are found at the end of string.
    string_data = re.sub(r'(?<![a-zA-Z])\.(?![a-zA-Z])', ' ', string_data)
    # Removing period and extra spaces in the middle of the string
    string_data = re.sub(r'\.\s+', ' ', string_data)
    #  Remove any leading or trailing spaces from
    clean_content = re.sub(r'\s+', ' ', string_data).strip()
    return clean_content


@st.cache_resource(show_spinner=False)
def modify_images(image_path: str, width: int, height: int) -> Image:
    """Read and resize images"""
    img = Image.open(image_path)
    resized_image = img.resize((width, height))
    return resized_image


@st.cache_resource(show_spinner=False)
def render_front_page_image() -> None:
    """Display the page image."""
    img_path = "./resource/site_images/wallpaper.png"
    img = modify_images(image_path=img_path, width=1000, height=400)
    st.image(img, use_column_width=True)


@st.cache_resource(ttl=timedelta(hours=1), show_spinner=False)
def read_text_file(user_file: TextIO) -> str:
    """Reads and returns a clean_data of text file"""
    string_content = " ".join([line.decode('utf-8') for line in user_file])
    clean_content = clean_string_content(string_content)
    return clean_content


@st.cache_resource(ttl=timedelta(hours=1), show_spinner=False)
def read_pdf_file(user_file: TextIO) -> tuple[int, str]:
    """Abstracts file content and returns page number(s) and clean_data of file."""
    list_content = []
    with st.spinner("Cleaning file content..."):
        pdfReader = PyPDF2.PdfReader(user_file)
        page_num = len(pdfReader.pages)
        for page in range(page_num):
            page_content = pdfReader.pages[page].extract_text()
            list_content.append(page_content)

    string_content = " ".join(list_content)
    clean_content = clean_string_content(string_content)
    return page_num, clean_content


@st.cache_resource(ttl=timedelta(hours=1), show_spinner=False)
def read_word_document(user_file: TextIO) -> str:
    """Reads and returns a clean_data of word documents"""
    doc = docx.Document(user_file)
    string_content = " ".join([paragraph.text for paragraph in doc.paragraphs])
    clean_content = clean_string_content(string_content)
    return clean_content
