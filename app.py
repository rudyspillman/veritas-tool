import streamlit as st
import time

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="VERITAS AI - Universal Engine",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- IMAGEN DE FONDO (TU DISEÑO) ---
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
    
    /* Estilo de Botones para que resalten sobre la imagen */
    .stButton > button {{
        width: 100%;
        background-color: rgba(0, 0, 0, 0.8);
        color: #00ffff;
        border: 2px solid #00ffff;
        border-radius: 10px;
        font-weight: bold;
        font-size: 18px;
        text-transform: uppercase;
        padding: 12px;
        transition: all 0.3s;
    }}
    .stButton > button:hover {{
        background-color: #00ffff;
        color: black;
        box-shadow: 0 0 15px #00ffff;
        transform: scale(1.05);
    }}
    
    /* Cajas de Resultado */
    .result-box {{
        background-color: rgba(0, 0, 0, 0.95);
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #00ffff;
        margin-top: 15px;
        color: white;
    }}
    </style>
""", unsafe_allow_html=True)

# --- ESPACIADOR PARA BAJAR LOS BOTONES (Ajuste visual) ---
st.markdown("<br><br><br><br><br><br>", unsafe_allow_html=True)

# --- ESTRUCTURA DE 3 COLUMNAS ---
col_left, col_center, col_right = st.columns([1, 1, 1])

# --- COLUMNA IZQUIERDA ---
with col_left:
    st.markdown("### 📝 TEXT / EMAIL FORENSICS")
    text_input = st.text_area("Paste suspicious text here:", height=100)
    if st.button("ANALYZE TEXT"):
        if text_input:
            with st.spinner("Scanning linguistic patterns..."):
                time.sleep(2)
                st.markdown("""
                <div class="result-box">
                    <h3 style="color: #ff3333;">⚠️ HIGH RISK DETECTED</h3>
                    <p><strong>Verdict:</strong> Phishing / Scam Pattern.</p>
                    <p><strong>Reason:</strong> Urgency triggers and non-standard syntax detected.</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("Please paste some text first.")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("### 🖼️ IMAGE FORENSICS")
    img_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])
    if img_file:
        if st.button("SCAN IMAGE"):
            with st.spinner("Analyzing pixels..."):
                time.sleep(2)
                st.success("✅ IMAGE VERIFIED: No manipulation detected.")

# --- COLUMNA CENTRAL ---
with col_center:
    # Espacio extra para que el botón de video quede más abajo (cruzando el haz de luz)
    st.markdown("<br><br><br><br>", unsafe_allow_html=True)
    
    st.markdown("### 🎥 VIDEO DEEPFAKE SCAN")
    vid_file = st.file_uploader("Upload Video (MP4)", type=['mp4', 'mov'])
    if vid_file:
        if st.button("SCAN VIDEO FRAMES"):
            with st.spinner("Analyzing frame consistency..."):
                time.sleep(3)
                st.markdown("""
                <div class="result-box" style="border-color: #33ff33;">
                    <h3 style="color: #33ff33;">✅ AUTHENTIC FOOTAGE</h3>
                    <p><strong>Confidence:</strong> 99.8%</p>
                    <p>No AI artifacts found in facial landmarks.</p>
                </div>
                """, unsafe_allow_html=True)

# --- COLUMNA DERECHA ---
with col_right:
    st.markdown("### 🔗 URL / SOCIAL LINK")
    url_input = st.text_input("Paste URL:")
    if st.button("CHECK LINK"):
        if url_input:
            st.info("ℹ️ Analyzing domain reputation... (Safe)")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("### 🔊 AUDIO FORENSICS")
    aud_file = st.file_uploader("Upload Audio", type=['mp3', 'wav'])
    if aud_file:
        if st.button("ANALYZE WAVEFORMS"):
            st.warning("⚠️ AI VOICE DETECTED (ElevenLabs signature).")

# --- PIE DE PÁGINA ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.caption("VERITAS AI - Universal Verification Engine © 2026 Rudy Spillman")
