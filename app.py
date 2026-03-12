import streamlit as st
from elevenlabs.client import ElevenLabs
import tempfile

client = ElevenLabs(api_key="YOUR_ELEVENLABS_API_KEY")

st.title("Voice AI Widget")

audio_data = st.audio_input("🎤 Click to record your question")

if audio_data is not None:
    st.write("Processing...")

    audio = client.text_to_speech.convert(
        text="Hello, how can I help you today?",
        voice_id="21m00Tcm4TlvDq8ikWAM"
    )

    output_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    with open(output_file.name, "wb") as f:
        for chunk in audio:
            f.write(chunk)

    st.audio(output_file.name)
