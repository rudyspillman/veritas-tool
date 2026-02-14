import streamlit as st
import time

st.set_page_config(page_title="VERITAS AI", layout="wide", initial_sidebar_state="collapsed")

# IMAGEN DE FONDO Y ESTILOS
background_url = "https://i.postimg.cc/Kzv816Jc/VERITAS_AI_Universal_Verification_Engine_IMAGEN.png"

st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("{background_url}");
        background-attachment: fixed;
        background-size: cover;
        background-position: center;
    }}
    #MainMenu, footer, header {{visibility: hidden;}}
    
    .stButton > button {{
        width: 100%;
        background-color: rgba(0, 0, 0, 0.7);
        color: #00ffff;
        border: 2px solid #00ffff;
        border-radius: 12px;
        font-weight: bold;
        font-size: 20px;
        padding: 15px;
        text-transform: uppercase;
    }}
    .stButton > button:hover {{
        background-color: #00ffff;
        color: black;
    }}
    .input-box {{
        background-color: rgba(0, 0, 0, 0.95);
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #00ffff;
        margin-top: 10px;
        margin-bottom: 20px;
    }}
    </style>
""", unsafe_allow_html=True)

st.markdown("<br><br><br><br><br>", unsafe_allow_html=True)

col_left, col_center, col_right = st.columns([1, 1, 1])

# INTERFAZ
with col_left:
    if st.button("📝 TEXT / EMAIL"):
        st.markdown('<div class="input-box">', unsafe_allow_html=True)
        st.text_area("Paste text:", height=100)
        st.button("Analyze Text")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br><br><br><br>", unsafe_allow_html=True)
    
    if st.button("🖼️ IMAGE"):
        st.markdown('<div class="input-box">', unsafe_allow_html=True)
        st.file_uploader("Upload Image", type=['jpg', 'png'])
        st.markdown('</div>', unsafe_allow_html=True)

with col_center:
    st.markdown("<br><br><br><br><br><br><br><br>", unsafe_allow_html=True)
    if st.button("🎥 VIDEO"):
        st.markdown('<div class="input-box">', unsafe_allow_html=True)
        st.file_uploader("Upload Video", type=['mp4'])
        st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    if st.button("🔗 URL / LINK"):
        st.markdown('<div class="input-box">', unsafe_allow_html=True)
        st.text_input("Paste URL")
        st.button("Check Link")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br><br><br><br>", unsafe_allow_html=True)

    if st.button("🔊 AUDIO"):
        st.markdown('<div class="input-box">', unsafe_allow_html=True)
        st.file_uploader("Upload Audio", type=['mp3'])
        st.markdown('</div>', unsafe_allow_html=True)
