import streamlit as st
import sounddevice as sd
import soundfile as sf
import os
import tempfile
from dotenv import load_dotenv, find_dotenv
from groq import Groq
from PIL import Image
import edge_tts
import asyncio

# Load environment variables
find_dotenv()
load_dotenv()

# Groq API client
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Functions
def record_audio(duration=5, sample_rate=44100):
    st.write("🎙️ Recording...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
    sd.wait()
    st.write("✅ Recording complete")
    return audio_data, sample_rate

def save_audio(audio_data, sample_rate):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    sf.write(temp_file.name, audio_data, sample_rate)
    return temp_file.name

def transcribe_audio_with_whisper(audio_file_path):
    try:
        with open(audio_file_path, "rb") as audio_file:
            response = groq_client.audio.transcriptions.create(
                model="whisper-large-v3",
                file=audio_file,
                language="en"
            )
            return response.text
    except Exception as e:
        st.error(f"❌ Transcription error: {e}")
        return None

def get_groq_response(prompt):
    try:
        response = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a helpful voice assistant. Reply in a clear Q&A format."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"❌ LLM error: {e}")
        return None

def text_to_speech(text):
    try:
        output_path = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3").name
        voice = "en-US-GuyNeural"  # ✅ Male voice
        asyncio.run(edge_tts.Communicate(text, voice).save(output_path))
        return output_path
    except Exception as e:
        st.error(f"❌ Text-to-speech error: {e}")
        return None

# --- UI Setup ---
st.set_page_config(page_title="Vision Assistant", layout="centered")

# Logo/Header
logo = "image.png"  # Your local avatar image
if os.path.exists(logo):
    col_logo, col_title = st.columns([1, 5])
    with col_logo:
        st.image(logo, width=60)
    with col_title:
        st.title("🔮 Digital Voice Assistant - Vision")
else:
    st.title("🔮 Digital Voice Assistant - Vision")

st.markdown("---")

# Layout
col1, col2 = st.columns(2)
with col1:
    st.subheader("🗣️ Your Input")
with col2:
    st.subheader("🤖 Assistant Output")

# --- Audio Input Option ---
if st.button("🔊 Speak Now (5 sec)"):
    audio_data, sample_rate = record_audio()
    audio_file = save_audio(audio_data, sample_rate)

    with col1:
        st.audio(audio_file, format="audio/wav")

    transcription = transcribe_audio_with_whisper(audio_file)
    os.unlink(audio_file)

    if transcription:
        with col1:
            st.markdown(f"🧙💬 **You:** {transcription}")

        response = get_groq_response(transcription)
        if response:
            with col2:
                st.markdown(f"🤖 **Assistant:** {response}")
                speech_file = text_to_speech(response)
                if speech_file:
                    st.audio(speech_file, format="audio/mp3")

# --- Text Input Option ---
text_input = st.text_input("💬 Ask anything:")
if text_input:
    with col1:
        st.markdown(f"🧙💬 **You:** {text_input}")

    response = get_groq_response(text_input)
    if response:
        with col2:
            st.markdown(f"🤖 **Assistant:** {response}")
            speech_file = text_to_speech(response)
            if speech_file:
                st.audio(speech_file, format="audio/mp3")
