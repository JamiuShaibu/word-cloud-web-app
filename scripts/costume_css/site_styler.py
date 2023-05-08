import streamlit as st


def style_background() -> None:
    """Styles the site background with an image"""
    st.markdown("""
        <style>
          .stApp {
            background: url("https://bit.ly/3RwnuLS");
            background-size: cover;
          }

          div[class="block-container css-z5fcl4 egzxvld4"] {
            padding-top: 15px !important;
            padding-bottom: 20px !important;
            bottom: 80px;
          }
          
          div[data-testid="collapsedControl"] {
            color: white
          }
            
          footer.css-164nlkn.egzxvld1 {
            visibility: hidden;
          }  
        </style>""", unsafe_allow_html=True)


def style_header() -> None:
    """Styles header"""
    st.markdown("""
        <style>
          header[data-testid="stHeader"][class="css-18ni7ap e8zbici2"] {
            color: white;
            background-color: #2B4865;
          }

          div[data-testid="collapsedControl"][class="css-y4qlto e1fqkh3o2"] {
            color: white;
          }
        </style>
        """, unsafe_allow_html=True)


def style_sidebar() -> None:
    """Styles sidebar"""
    st.markdown("""
        <style>
          section[data-testid="stSidebar"][aria-expanded="true"] {
            # background-image: linear-gradient(#4ddef58f,#8993ab);
            color: white;
            width: 272px !important;           
          }
            
          section[data-testid="stSidebar"][aria-expanded="false"] {
            # background-image: linear-gradient(#f55f4d,#8993ab);
            color: white;
            width: 272px !important;           
          }
        </style>""", unsafe_allow_html=True)


def style_uploader_container() -> None:
    """Styles file uploader container"""
    st.markdown("""
        <style>
          div[class="uploadedFile css-12xsiil exg6vvm5"] {
            color: rgb(248 249 251);
            background-color: black;
            font-weight: bold;
          }

          small[class="css-1aehpvj euu6i2w0"] {
            color: wheat;
          }

          small[class="css-aoozme exg6vvm2"] {
            color: red;
            font-weight: bold;
          }
        </style>""", unsafe_allow_html=True)


def style_uploader_button() -> None:
    """Styles file uploader container button"""
    st.markdown("""
    <style>
      div.stButton{
        text-align: center;
        margin-bottom: -10px;
      }

      div.stButton > button:first-child {
        background-color: #2B4865;
        border: 3px solid #e7bfb1;
        border-radius: 9px;
        color: aliceblue;
      }

      button[class="css-1cysak7 edgvbvh10"][kind="secondary"] {
        background-color: #2B4865 !important;
        color: aliceblue;
        font-weight: bold;
      }
      
      .css-1x8cf1d {
        border-color: wheat;
        color: aliceblue;
        font-weight: bold;
        background-color: #2B4865 !important;
      }
      
      .css-1x8cf1d:hover {
        color: aliceblue;
      }
    </style>""", unsafe_allow_html=True)


def style_input_fields() -> None:
    """Styles input fields and generated image container"""
    st.markdown("""
        <style>
          label[class="css-15tx938 effi0qh3"] {
            font-weight: bold;
            font-size: 15px;
            margin-bottom: -0.1em;
          }

          div.css-1kyxreq {
            justify-content: center !important;
          }
        </style>""", unsafe_allow_html=True)


def style_button() -> None:
    """Styles Button"""
    st.markdown("""
    <style>
      label[class="css-15tx938 effi0qh3"] {
        font-weight: bold;
      }

      div.stButton > button:hover {
        border: 3px solid #b1bfe7;
        background-color: #66ffcc; 
        box-shadow: 0px 2px 5px rgb(6, 18, 19);
        # transform: translateY(-5px);
        text-weight: bold;
      } 
    </style>""", unsafe_allow_html=True)


def style_download_button() -> None:
    """Styles radio and Download Button"""
    st.markdown("""
    <style>
      .generatedImageH {
        text-align: center; 
        color: #4C4C6D; 
        margin-bottom: -30px;
      }
    
      div[role="radiogroup"] {
        display: flex;
        flex-direction: inherit;
        position: relative;
        bottom: 35px;
        justify-content: center;
        margin-bottom: -40px;
      }
    
      @media only screen and (max-width: 768px) {
        div[role="radiogroup"] {
         bottom: 45px;
         margin-bottom: -50px;
        }
      }
      
      @media only screen and (max-width: 425px) {
        .generatedImageH {
          margin-bottom: -25px; 
          padding-bottom: 0;
        }
        
        div[role="radiogroup"] {
         bottom: 55px;
         margin-bottom: -60px;
        }
      }
    
      div.stDownloadButton {
        margin-top:-5px;
        text-align: center;
      }
        
      div.stDownloadButton > button:first-child {
        background-color: #F0F2F6 !important;
        transition: all 0.3s ease 0s;
        border-radius: 9px;
        border: 3px solid #e7bfb1;
        color: #31333F;
        padding: 0.5em; 
        height: 46px;
      }
        
      div.stDownloadButton > button:hover {
        background-color: #2B4865 !important;
        box-shadow: 0px 2px 5px rgb(6, 18, 19);
        border: 3px solid #b1bfe7;
        border-radius: 9px;
        # transform: translateY(-5px);
        color: #ffffff;
      }
    </style>""", unsafe_allow_html=True)
