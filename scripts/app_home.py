from page_content.footer import footer_html
from page_content.about import about_app_html
from costume_css.site_styler import style_sidebar, style_download_button, style_button, \
    style_header, style_background, style_input_fields

from helper_functions import render_front_page_image
from word_cloud import project_handler
import streamlit as st


def sidebar_items() -> None:
    """Display sidebar items"""
    style_sidebar()
    about_app_html()


def load_page() -> None:
    st.set_page_config(layout="wide", page_icon="🪶", page_title="Wordcloud-Generator")
    sidebar_items()
    style_background()
    style_header()
    style_input_fields()
    style_button()
    style_download_button()
    render_front_page_image()
    project_handler()
    footer_html()


if __name__ == "__main__":
    load_page()
