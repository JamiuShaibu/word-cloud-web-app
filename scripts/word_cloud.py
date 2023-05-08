from datetime import datetime, timedelta
from io import BytesIO
from typing import Tuple, TextIO

import streamlit as st
from PIL.Image import Image
from langdetect import LangDetectException
from wordcloud import WordCloud

from helper_functions import read_text_file, read_pdf_file, read_word_document
from project_modules.color_hub import get_image_colors

from page_content.faq_content import faq_html_content
from project_modules.stopwords_getter import set_stopwords_base_on_content_language
from costume_css.site_styler import style_uploader_button, style_uploader_container


@st.cache_resource(ttl=timedelta(hours=1), show_spinner=False)
def process_uploaded_file(user_file: TextIO) -> Tuple[str, str]:
    """Takes uploaded file as parameter and returns a cleaned up string"""
    file_content = ""
    file_extension = user_file.name.split(".")[1].lower()
    page_number_html = ""
    if file_extension == "pdf":
        default_page_num = 1
        page_num, file_content = read_pdf_file(user_file)
        if page_num > default_page_num:
            page_number_html = f"""
                <h5 style="font-family: 'Times New Roman', serif; margin-top: -10px">
                    File contains {page_num} pages.
                </h5>"""
        else:
            page_number_html = f"""
                <h5 style="font-family: 'Times New Roman', serif; margin-top: -10px">
                    File contains only {page_num} page.
                </h5>"""
    elif file_extension == "txt":
        file_content = read_text_file(user_file)
    elif file_extension == "docx":
        file_content = read_word_document(user_file)
    return page_number_html, file_content


@st.cache_resource(ttl=timedelta(hours=1), show_spinner=False)
def generate_and_render_image(cleaned_data: str, image_color: str, width_input: int, height_input: int) -> Image:
    """Generates, renders and returns image"""
    new_stopwords_list = set_stopwords_base_on_content_language(cleaned_data)
    Wcloud = WordCloud(
        background_color=image_color,
        stopwords=new_stopwords_list,
        height=height_input,
        width=width_input,
    )

    image = None
    try:
        with st.spinner("Generating word-cloud..."):
            # Generate wordcloud using file content
            Wcloud.generate(cleaned_data)

        image = Wcloud.to_image()
        st.markdown('''
            <h3 class='generatedImageH'>
                Image Successfully Generated!
            </h3>''', unsafe_allow_html=True)
        left, middle, right = st.columns((1, 10, 1))
        with middle:
            st.image(image)
    except ValueError:
        st.warning("**Note:** Width and Height must be **above 20 pixels** for better user experience. You can "
                   "refer to our **FAQ** below for more information on Standard image pixels. Thank You!")
    return image


def render_download_button(received_img: Image, width: int, height: int) -> None:
    # Convert image to bytes and store in memory
    if received_img:
        extension = st.radio("Download Image as:",
                             ('PNG', 'JPEG'), label_visibility="hidden")
        image_bytes = BytesIO()
        received_img.save(image_bytes, format=extension)
        image_bytes.seek(0)

        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y-%H-%M-%S")
        download_filename = f"{width}X{height}_jamiu_wordcloud_img_{dt_string}.{extension.lower()}"

        st.download_button(file_name=download_filename,
                           label=f"📥Download {extension} Image",
                           data=image_bytes.getvalue(),
                           mime=f"image/{extension.lower()}")


def project_handler() -> None:
    """Holds the project functionality"""
    style_uploader_button()
    style_uploader_container()
    uploaded_file = st.file_uploader("Upload a file", type=["pdf", "txt", "docx"])

    col1, col2, col3 = st.columns(3)
    colors = get_image_colors()
    with col1:
        image_color = st.selectbox("Pick Image Color:", colors)
    with col2:
        width_input = st.number_input("Enter Image Width:", value=0, min_value=0, max_value=3840)
    with col3:
        height_input = st.number_input("Enter Image Height:", value=0, min_value=0, max_value=2160)

    # Renders total number of pages in the file
    render_page_number = st.container()

    # Initialize a session state for button
    generateButton = st.button("Auto Generate Word Cloud")
    if "generate_generateButton" not in st.session_state:
        st.session_state["generate_generateButton"] = False
    if generateButton or st.session_state["generate_generateButton"]:
        st.session_state["generate_generateButton"] = True

    # When generateButton is clicked, clear the cache of this function in order to generate new image
    if generateButton:
        generate_and_render_image.clear()

    clean_data = ""
    if uploaded_file:
        page_number, clean_data = process_uploaded_file(uploaded_file)
        render_page_number.markdown(page_number, unsafe_allow_html=True)

    default_pixel = 0
    if uploaded_file and (height_input and width_input != default_pixel):
        try:  # Try to get content language else write error message to end-user
            image = generate_and_render_image(clean_data, image_color, width_input, height_input)
            render_download_button(image, width_input, height_input)
        except LangDetectException:
            st.error("File content is not supported. Please try a different file.")

    elif uploaded_file is None and generateButton:
        st.info("Please you are required to upload a file and fill in the input fields.")
    elif uploaded_file and generateButton:
        st.info("Please make sure you fill all the input fields.")

    with st.expander("**Read FAQs:**"):
        st.markdown(faq_html_content, unsafe_allow_html=True)
