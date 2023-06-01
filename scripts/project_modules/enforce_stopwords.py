import streamlit as st


@st.cache_resource(show_spinner=False)
def provide_more_stopwords(language: str) -> list[str]:
    """
    Returns a list of more stopwords which are not in nltk stopwords.
    A new language and a list of your preferred stopwords can be added to this dictionary
    """
    stopwords = {
        "english": [
            'doi', 'also', 'often', 'see', 'could', 'seem', 'others', 'us', 'https', 'www', 'said', 'end',
            'next', 'likely', 'whether', 'another', 'going', 'go', 'without', 'would', 'doing', 'someone',
            'one', 'thing', 'two', 'no', 'Whenever', 'every', 'something', 'somethings', 'things', 'used',
            'com', 'However', 'rather', 'still', 'put', 'que', 'p', 'la', 'de', 'pp', 'Thus', 'ed', 'en',
            'vol', 'th', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
            'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'seems',
            'come', 'Come', 'whenever', 'three', 'yet', 'way', 'TXT', 'txt', 'pc', 'either', 'ing', 'else',
            'ever', 'therefore', 'le', 'ly', 'es', 'er', 'oin', 'sa', 'ent', 'od', 'although', 'ye', 'thy',
            'Fo', 'though', 'ng', 'hath', 'thee', 'unto', 'whatever', 'Thou',
        ],
        "spanish": [
            'solo', 'somos', 'tan', 'aun', 'mismo', 'misma', 'mas', 'si', 'sere', 'veras', 'aqui', 'ser',
            'veía', 'miró', 'dos', 'casi', 'aún', 'tal', 'pues', 'ambos', 'cada', 'ahí', 'allá', 'hacía',
            'hacia', 'vio', 'ir', 'paso', 'Además', 'tomó', 'iba', 'pasó', 'así', 'después', 'aunque',
            'debía', 'dejo', 'cosa', 'cómo', 'tipo', 'va', 'par', 'punto', 'voy', 'ver', 'rato', 'vez',
            'dio', 'sido', 'vas', 'aquella', 'debía', 'veces', 'abrió', 'dejó', 'podía', 'sabe', 'cosas',
            'podría', 'aquello', 'sabes', 'sabía', 'aquí', 'aquel', 'entonces', 'hecho', 'hace', 'hizo',
            'B', 'hacer', 'Ah', 'debe', 've', 'unas', 'vamos', 'haber', 'allí', 'dicho', 'mientras', 'quién',
            'echo', 'algún', 'dijo', 'dice', 'vi', 'digo', 'toda', 'todo', 'veo', 'puedo', 'dije', 'sola',
            'solo', 'solas', 'solos', 'usted', 'sólo', 'dónde', 'echó', 'tres', 'cuatro', 'sinco', 'seis',
            'ocho', 'nueve', 'in', 'n', 'c', 'ello', 'ta', 'tal', 'ba', 'h', 'a', 'b', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'as', 'etc',
            'au', 'be', 'ne', 're', 'ra', 'na', 'jo', 'tra', 'ca', 'usté', 'sa', 'co', 'ro', 'des', 'lado',
            'pa', 'an', 'to', 'todas', 'todos', 'iban', 'vió', 'tras', 'dar', 'Jos', 'fué', 'ésta', 'nte',
            'éste', 'of', 'is', 'there', 'the', 'éstos', 'siete', 'so', 'Do', 'do', 'and', 'this', 'those'
        ],
        "german": [
            'beim', 'P', 'jedoch', 'ging', 'darauf', 'c', 'deren', 'kam', 'm',
        ]
    }
    return stopwords.get(language, ['brrr'])
