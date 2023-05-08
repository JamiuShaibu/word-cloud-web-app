import streamlit as st


@st.cache_resource(show_spinner=False)
def about_app_html() -> None:
    st.markdown("""
    <style>
        a {
          color: #002B5B !important;
        }
        
        a:hover {
          color: #4e4800 !important;
        }
        
        h1 {
          color: #002B5B; 
          text-align: center; 
          font-weight: bold;
          padding-top: 0; 
          margin-top: -10px
        }
        
        h4 {
          text-align: center;  
          font-family: Brush Script MT, cursive;
          padding-bottom: 10px; 
        }
        
        .stars {
          text-align: center; 
          font-weight: bold; 
          margin-top: -56px; 
        }
        
        .description {
          color: black; 
          font-size: 100%; 
          font-weight: bold; 
          margin-top: -10px; 
          margin-bottom: 0;
          text-align: center;
        }
        
        .links-container {
          display: flex;
          position: relative;
          bottom: 10px;
          flex-direction: column;
          justify-content: center; 
          margin-bottom: -20px; 
          align-items: center;
          padding-top: 5px;
        }
        
        .links-container ul {
          display: flex;
          justify-content: center;
          align-items: center;
          margin: 0
        }
        
        .links-container li {
          display: block;
          padding: 0;
          margin: 0;
        }
        
        .coffee {
          width: 120px;
        }
        
        .link-image { 
          padding: 10px;
          width: 45px;  
          transition: transform .2s;
        }
        
        .link-image:hover {  
          transform: scale(1.2);
          transition: 0.2s;
        }
        
        .line-dis {
          border-width:7px; 
          background-color:#2B4865;
          margin-right: -16px; 
          margin-left: -16px; 
          padding-bottom: 17px;
          margin-top: -85px
        }
        
        @media only screen and (max-width: 1024px) {
          .links-container {
            padding-bottom: 45px;
          }
        }
        
        @media only screen and (max-width: 768px) {
          .links-container {
            padding-bottom: 25px;
          }
        }
        
    </style>
    """, unsafe_allow_html=True)
    st.sidebar.markdown("""
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>About</title>
  </head>
  <body>
    <hr class="line-dis">
    <p class="stars">☆☆☆☆☆☆☆☆☆☆</p>
    <h1><u>ABOUT</u></h1>
    <p class="description">
      This application is designed to generate word cloud images from user-uploaded PDF, TXT, or DOCX files. 
      It processes the file and generates a word cloud image that visually represents the most 
      frequently used words in the document.
      <br>
      <br>
      <strong style="color:black">☆</strong> The application gives users the flexibility to enter their own 
      desired image <strong><em>color, width and height</em></strong>.
      <br>
      <br>
      <strong style="color:black">☆</strong> Clicking the 'Auto Generate Word Cloud' button produces an image 
      with randomized text formation.
    </p>
    <div class="links-container">
      <h4><a href="mailto:jamiushaibu12@gmail.com" target="_blank">Developer; Jamiu Shaibu</a></h4>
      <ul>
          <li>
            <a href="https://github.com/JamiuShaibu" target="_blank">
              <img class="link-image" 
                src="https://www.freeiconspng.com/uploads/github-logo-icon-22.png" 
                alt="stackoverflow icon">
            </a>
          </li>
          <li>
            <a href="https://stackoverflow.com/users/19290081/jamiu-shaibu" target="_blank">
              <img class="link-image" 
                src="https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/stackoverflow-color-icon.svg" 
                alt="stackoverflow icon">
            </a>
          </li>
          <li>
            <a href="https://www.linkedin.com/in/jamiu-shaibu-9037ba195/" target="_blank">
              <img class="link-image" 
                src="https://cdn-icons-png.flaticon.com/512/174/174857.png" 
                alt="linkedin icon">
            </a>
          </li>
          <li>
            <a href="https://twitter.com/Prince__jam" target="_blank">
              <img class="link-image" 
                src="https://pngimg.com/uploads/twitter/twitter_PNG22.png" 
                alt="twitter icon">
            </a>
          </li>
      </ul>
      <ul>
        <a href="https://www.buymeacoffee.com/jamiushaib5" target="_blank">
          <img class="coffee" src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee">
        </a>
      </ul>
    </div>
  </body>
</html>""", unsafe_allow_html=True)
