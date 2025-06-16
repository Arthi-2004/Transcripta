import streamlit as st
import whisper
import tempfile
import os

# Ensure FFMPEG path (only required locally, not on Streamlit Cloud)
os.environ["PATH"] += os.pathsep + r"C:\Users\ADMIN\Downloads\ffmpeg-7.1.1-essentials_build\ffmpeg-7.1.1-essentials_build\bin"

st.set_page_config(page_title="🎙️ Audio Caption Tool", layout="centered")
st.title("🗣️ AI-Powered Caption Generator")
st.subheader("Upload your audio file to generate accurate captions")

# Load Whisper model
@st.cache_resource
def load_model():
    return whisper.load_model("base")

model = load_model()

# Upload audio mode only
uploaded_file = st.file_uploader("Upload audio (.mp3, .wav, .m4a):", type=["mp3", "wav", "m4a"])
if uploaded_file:
    st.audio(uploaded_file)

    if st.button("📝 Generate Captions"):
        with st.spinner("Transcribing using Whisper..."):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
                temp_audio.write(uploaded_file.read())
                temp_path = temp_audio.name

            result = model.transcribe(temp_path)
            transcription = result["text"]
            os.remove(temp_path)

        st.success("✅ Transcription Complete!")
        st.markdown("### 📋 Captions")
        st.write(transcription)

st.markdown("---")
st.caption("Made with ❤️ for 3Percent Hacks - Building with AI")
