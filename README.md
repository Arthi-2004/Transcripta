# Transcripta
AI-Powered Live Captioning Tool
A Real-Time Speech Transcription & Audio Caption Generator built using OpenAI Whisper, Google Speech Recognition, and Streamlit. Designed for meetings, accessibility tools, and audio summarization.

# 🚀 Features
🎧 Upload audio files (.mp3, .wav, .m4a) and generate captions using Whisper

🎤 Real-time speech-to-text from microphone input using Google STT

🔁 Chunk-wise live transcription for meetings

💬 Full transcript generated at the end

✅ FFmpeg-integrated backend for audio processing

# Requirements
Python 3.8+

FFmpeg (must be added to system PATH)

Install dependencies:
pip install -r requirements.txt

# Tech Stack
Tool	Purpose
Whisper	Audio transcription (offline)
Google STT	Real-time mic transcription
Streamlit	UI for web interface
FFmpeg	Audio processing backend

# ▶️ How to Run Locally
Clone the repository:
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# Install requirements:
pip install -r requirements.txt
Make sure FFmpeg is installed and added to your system PATH.

# Run the Streamlit app:
streamlit run App.py

# 📂 File Structure
📁 your-project/
│
├── App.py                  # Main Streamlit app
├── requirements.txt        # All Python dependencies
└── README.md               # You're reading this!

# 💡 Inspiration
This project was built as part of the 3Percent Hacks - Building with AI hackathon.
Designed to bridge accessibility gaps and support real-time captioning for audio-based communication.
