import streamlit as st


@st.cache_resource(show_spinner=False)
def provide_more_stopwords(language: str) -> list[str]:
    """
    Returns a list of more stopwords which are not in nltk stopwords.
    A new language and a list of your preferred stopwords can be added to this dictionary
    """
    stopwords = {
        "english": [
            'doi', 'also', 'often', 'much', 'even', 'see', 'could', 'seem', 'others', 'us', 'https',
            'www', 'said', 'end', 'next', 'likely', 'whether', 'another', 'going', 'go', 'without',
            'would', 'doing', 'someone', 'one', 'thing', 'two', 'no', 'Whenever', 'every', 'second',
            'seconds', 'something', 'somethings', 'things', 'used', 'com', 'However', 'rather', 'still',
            'put', 'que', 'p', 'la', 'de', 'pp', 'las', 'Thus', 'ed', 'en', 'vol', 'th', 'a', 'b', 'c',
            'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
            'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'seems', 'come', 'Come', 'whenever',
            'three', 'yet', 'way', 'TXT', 'txt', 'pc', 'either', 'ing', 'else', 'ever', 'therefore',
        ],
        "spanish": [
            'solo', 'somos', 'tan', 'aun', 'mismo', 'misma', 'mas', 'si', 'sere', 'veras', 'aqui', 'ser',
            'veía', 'miró', 'dos', 'casi', 'aún', 'tal', 'pues', 'ambos', 'cada', 'ahí', 'allá', 'hacía',
            'hacia', 'vio', 'ir', 'paso', 'Además', 'decidió', 'tomó', 'iba', 'pasó', 'así', 'después',
            'aunque', 'debía', 'dejo', 'cosa', 'cómo', 'tipo', 'va', 'par', 'punto', 'voy', 'ver', 'rato',
            'vez', 'dio', 'comenzó', 'sido', 'vas', 'aquella', 'debía', 'veces', 'abrió', 'contestó', 'dejó',
            'podía', 'sintió', 'sabe', 'cosas', 'podría', 'pensaba', 'giró', 'pensó', 'preguntó', 'aquello',
            'sabes', 'sabía', 'volvió', 'siguió', 'aquí', 'aquel', 'explicó', 'caminó', 'quedó', 'llevó',
            'encontró', 'entonces', 'hecho', 'hace', 'hizo', 'B', 'hacer', 'Ah', 'debe', 've', 'unas', 'vamos',
            'haber', 'allí', 'dicho', 'mientras', 'quién', 'echo', 'algún', 'dijo', 'dice', 'vi', 'digo', 'toda',
            'todo', 'veo', 'puedo', 'dije', 'sola', 'solo', 'solas', 'solos', 'usted', 'sólo', 'dónde', 'echó',
            'tres', 'cuatro', 'sinco', 'seis', 'siete', 'ocho', 'nueve', 'diez', 'in', 'n', 'c', 'ello', 'ta',
            'tal', 'ba', 'h', 'a', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'as', 'au', 'be', 'ne', 're', 'ra', 'na', 'jo', 'tra', 'ca', 'usté',
            'sa', 'co', 'ro', 'des', 'lado', 'pa', 'an', 'to', 'todas', 'todos', 'iban', 'vió', 'tras', 'dar',
            'Jos', 'fué', 'ésta', 'nte'
        ]
    }
    return stopwords.get(language, ['brrr'])
