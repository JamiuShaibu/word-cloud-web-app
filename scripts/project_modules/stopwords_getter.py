import streamlit as st
from datetime import timedelta
from typing import Optional

from langdetect import detect_langs
from nltk.corpus import stopwords
from .enforce_stopwords import provide_more_stopwords

import nltk
nltk.download('stopwords')


@st.cache_resource(ttl=timedelta(hours=1), show_spinner=False)
def map_language(abbr: str) -> str:
    LANGUAGES = {
        'ar': 'arabic',
        'az': 'azerbaijani',
        'da': 'danish',
        'nl': 'dutch',
        'en': 'english',
        'fi': 'finnish',
        'fr': 'french',
        'de': 'german',
        'el': 'greek',
        'hu': 'hungarian',
        'id': 'indonesian',
        'it': 'italian',
        'kk': 'kazakh',
        'ne': 'nepali',
        'no': 'norwegian',
        'pt': 'portuguese',
        'ro': 'romanian',
        'ru': 'russian',
        'sl': 'slovene',
        'es': 'spanish',
        'sv': 'swedish',
        'tg': 'tajik',
        'tr': 'turkish',
        'eu': 'basque',
        'bn': 'bengali',
        'ca': 'catalan',
        'zh-cn': 'chinese',
        'zh-tw': 'chinese',
        'iw': 'hebrew',
        'he': 'hebrew',
    }
    return LANGUAGES.get(abbr, None)


@st.cache_resource(ttl=timedelta(hours=1), show_spinner=False)
def set_stopwords_base_on_content_language(file_content: str) -> Optional[set]:
    """Get content language and add more stopwords to the nltk stopwords"""
    get_file_language = detect_langs(file_content)

    language_abbr = ""
    for language_data in get_file_language:
        language_abbr = str(language_data).split(":")[0]

    language = map_language(language_abbr)
    stop_words = set(stopwords.words(language))

    # Re-enforce stop words
    add_stopwords = provide_more_stopwords(language)
    stop_words = stop_words.union(add_stopwords)
    return stop_words
