import streamlit as st


@st.cache_resource
def footer_html():
    st.markdown("""
     <style>
        .img {
          max-width: 100%;
        }
        
        .footer {
          justify-content: center;
          align-items: center;
          width: -webkit-fill-available;
          padding-bottom: 5px;
          width: 100%;
          left: 0;
          bottom: 0;
          background-color: #268496;
          padding-bottom: 45px;
          position: relative;
          
        }
        
        .animation {
          display: flex;
          justify-content: center;
          border-radius: 4px;
          overflow: hidden;
        }
        
        .animation:after {
          display: flex;
          justify-content: center;
          align-items: center;
          content: '';
          position: absolute;
          background: #eeebda;
          color:black;
          font-size: 200%;
          width: 30%;
          height: 100%;
          border-radius: 2px;
          box-shadow: 0 0 5px rgba(0, 0, 0, .7);
          animation: load 10s infinite;
        }
        
        @keyframes load {
          0% {
          content: 'Full-Stack';
          font-style: italic;
          }

          20% {
          content: 'Word-Cloud';
          font-style: italic;
          }

          40% {
          content: 'Generator';
          font-style: italic;
          }

          60% {
          content: 'Engineering';
          font-style: italic;
          }

          80% {
          content: 'Premium';
          font-style: italic;
          }

          100% {
          content: 'Ui-Ux';
          font-style: italic;
          }
          
          120% {
          }
      </style>""", unsafe_allow_html=True)

    st.markdown("""
    <style>
        @media(min-width: 1024px) {
          .footer {
            background-color: #268496;
            justify-content: center;
            display: flex;
            align-items: center;
            position: relative;
            top: 120px;
            }
        }
        
        @media(max-width: 1023px) {
          .footer {
            display: flex;
            position: fixed;
            z-index: 999991;
          }
        }
        
        @media(max-width: 768px) {
          .footer{
             padding-bottom: 30px;
          }
          .animation:after {
            font-size: 120%;
          }
        }
        
        @media(max-width: 320px) {
          .animation:after{
            width: 38%;
          }
        }
        
        div[data-testid="stExpander"] {
            position: relative;
            top: 100px;
            # background-color: white
          }
    </style>
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="utf-8" />
        <title>Footer</title>
      </head
      <body>
        <div class="footer">
          <div class="animation"></div>
        </div>
      </body>
    </html>
    """, unsafe_allow_html=True)
