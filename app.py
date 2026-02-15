import streamlit as st
import base64
import datetime

# =========================
# CONFIGURACIÓN
# =========================
st.set_page_config(
    page_title="VERITAS AI — Universal Verification Engine",
    layout="wide"
)

# =========================
# HEADER
# =========================
st.title("VERITAS AI — Universal Verification Engine")
st.markdown("Analyze text, documents, and media for manipulation, fraud, and AI generation.")

# =========================
# SESSION STATE
# =========================
if "history" not in st.session_state:
    st.session_state.history = []

# =========================
# MODO DE ENTRADA
# =========================
mode = st.radio(
    "Select Analysis Mode",
    ["Text Analysis", "Media Upload"]
)

st.divider()

input_text = None
uploaded_file = None

# =========================
# TEXT MODE
# =========================
if mode == "Text Analysis":
    input_text = st.text_area(
        "Paste suspicious text, email, or contract:",
        height=250
    )

# =========================
# FILE MODE
# =========================
if mode == "Media Upload":
    uploaded_file = st.file_uploader(
        "Upload Image, Audio, Video or PDF (Max 10MB)",
        type=["png", "jpg", "jpeg", "mp3", "wav", "mp4", "pdf"]
    )

    if uploaded_file is not None:
        if uploaded_file.size > 10 * 1024 * 1024:
            st.error("File exceeds 10MB limit.")
            uploaded_file = None
        else:
            st.success(f"File ready: {uploaded_file.name}")

st.divider()

# =========================
# ANALYSIS BUTTON
# =========================
if st.button("VERIFY"):
    if not input_text and not uploaded_file:
        st.error("Provide text or upload a file.")
    else:
        with st.spinner("Running forensic protocols..."):
            # Simulación básica (aquí conectarías tu modelo real)
            result = {
                "verdict": "Authentic",
                "score": 87,
                "timestamp": datetime.datetime.now()
            }

            st.session_state.history.insert(0, result)

        st.success("Analysis Complete")

        st.subheader("Result")
        st.write(f"Verdict: {result['verdict']}")
        st.write(f"Confidence Score: {result['score']}%")
        st.write(f"Timestamp: {result['timestamp']}")

# =========================
# HISTORY
# =========================
if st.session_state.history:
    st.divider()
    st.subheader("Recent Analyses")

    for item in st.session_state.history[:3]:
        st.write(
            f"{item['timestamp'].strftime('%H:%M:%S')} — "
            f"{item['verdict']} ({item['score']}%)"
        )
