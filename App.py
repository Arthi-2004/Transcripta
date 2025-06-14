import streamlit as st
import whisper
import speech_recognition as sr
import tempfile
import os
import time

# Ensure FFMPEG path
os.environ["PATH"] += os.pathsep + r"C:\Users\ADMIN\Downloads\ffmpeg-7.1.1-essentials_build\ffmpeg-7.1.1-essentials_build\bin"

st.set_page_config(page_title="🎙️ Audio Caption Tool", layout="centered")
st.title("🗣️ AI-Powered Caption Generator")
st.subheader("Choose between real-time speech or audio upload")

@st.cache_resource
def load_model():
    return whisper.load_model("base")

model = load_model()

# Session state for controlling live recording
if "recording" not in st.session_state:
    st.session_state.recording = False
if "transcript" not in st.session_state:
    st.session_state.transcript = ""

option = st.radio("Choose a mode:", ["🎧 Upload Audio File", "🎤 Real-Time Speech Caption"])

# === Mode 1: Upload Audio ===
if option == "🎧 Upload Audio File":
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

            st.success("✅ Done!")
            st.markdown("### 📋 Captions")
            st.write(transcription)

# === Mode 2: Real-Time Speech ===
elif option == "🎤 Real-Time Speech Caption":
    st.markdown("### 🎙️ Control Live Captioning")

    col1, col2 = st.columns(2)
    start_btn = col1.button("▶️ Start Recording")
    stop_btn = col2.button("⏹️ Stop Recording")

    if start_btn:
        st.session_state.recording = True
        st.session_state.transcript = ""

    if stop_btn:
        st.session_state.recording = False

    if st.session_state.recording:
        recognizer = sr.Recognizer()
        mic = sr.Microphone()

        st.info("🎧 Listening... Speak now. Recording in 10-second chunks. Click STOP to end.")

        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            chunk_num = 1
            while st.session_state.recording:
                try:
                    st.markdown(f"🔊 Listening... (Chunk {chunk_num})")
                    audio_data = recognizer.listen(source, phrase_time_limit=10)

                    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
                        temp_audio.write(audio_data.get_wav_data())
                        temp_path = temp_audio.name

                    result = model.transcribe(temp_path)
                    chunk_text = result["text"]
                    st.session_state.transcript += chunk_text + " "
                    st.write(f"📝 {chunk_text}")
                    os.remove(temp_path)
                    chunk_num += 1
                except Exception as e:
                    st.warning(f"⚠️ Error: {e}")
                    break

    # Final transcript
    if st.session_state.transcript:
        st.markdown("### 🧾 Full Transcript")
        st.write(st.session_state.transcript)

st.markdown("---")
st.caption("Made with ❤️ for 3Percent Hacks - Building with AI")
