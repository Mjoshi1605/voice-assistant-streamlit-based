# 🔮 Digital Voice Assistant - Vision

A powerful Streamlit-based voice assistant that combines voice interaction, AI processing, and text-to-speech capabilities, powered by Groq AI and Edge TTS.

## ✨ Key Features

- 🎙️ Voice Input Capabilities
  - Real-time 5-second audio recording
  - High-quality audio capture at 44.1kHz
  - Temporary file handling for efficient processing

- 🤖 AI Processing
  - Groq LLaMA 3.3 70B model integration
  - Context-aware responses
  - Temperature-controlled output (0.7)
  - 500 token response limit for concise answers

- 🗣️ Speech Processing
  - Whisper Large V3 for accurate transcription
  - Edge TTS with male voice (en-US-GuyNeural)
  - MP3 output format for responses

- 📱 User Interface
  - Clean two-column layout
  - Real-time audio playback
  - Visual feedback during recording
  - Custom avatar support
  - Markdown formatting for responses

## 🛠️ Technical Stack

- **Frontend**: Streamlit
- **Audio Processing**: sounddevice, soundfile
- **AI Services**: Groq API
- **Speech Services**: Edge TTS, Whisper
- **File Handling**: tempfile, os
- **Configuration**: python-dotenv

## 📋 Requirements

### System Requirements
- Python 3.8 or higher
- Audio input device
- Internet connection for API services
- 4GB RAM minimum
- 100MB free disk space

### API Requirements
- Active Groq API account
- Valid API key with access to:
  - LLaMA 3.3 70B model
  - Whisper Large V3 model

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/chatbot-vision.git
```

```markdown:README.md
2. Install required packages:
```bash
pip install streamlit sounddevice soundfile python-dotenv groq pillow edge-tts
```

```markdown:README.md
3. Configure environment:
```bash
echo "GROQ_API_KEY=your_api_key_here" > .env
```

## 💻 Usage Examples

### Voice Interaction
1. Click "Speak Now"
2. Speak your question clearly
3. Wait for AI processing
4. Receive audio and text response

### Text Interaction
1. Type your question
2. Press Enter
3. Review the response
4. Listen to audio playback

## 🔧 Advanced Configuration

### Audio Settings
- Sample rate: 44100 Hz
- Channels: 1 (mono)
- Recording duration: 5 seconds
- Format: WAV (recording), MP3 (response)

### AI Parameters
- Temperature: 0.7
- Max tokens: 500
- Model: llama-3.3-70b-versatile
- System prompt: Voice assistant mode

## 📁 Project Structure

```
chatbot-vision/
├── app.py              # Main application
├── image.png           # Assistant avatar
├── .env                # Configuration
├── requirements.txt    # Dependencies
└── README.md          # Documentation
```

## 🔍 Troubleshooting

Common solutions:
- Check microphone permissions
- Verify API key validity
- Ensure stable internet connection
- Clear browser cache if UI issues occur
- Check audio device settings

## 🔄 Updates and Maintenance

Regular tasks:
- Update dependencies monthly
- Check API compatibility
- Monitor API usage
- Backup configuration files
- Test audio devices

## 📈 Performance Optimization

Tips for best performance:
- Use wired internet connection
- Close unnecessary browser tabs
- Update Python packages regularly
- Monitor system resources
- Clear temporary files periodically

## 🤝 Community and Support

- Report issues on GitHub
- Join discussions
- Share feature requests
- Contribute improvements
- Follow update announcements

## 📜 License

MIT License - Feel free to use and modify while maintaining attribution.

## 🏆 Credits

- Groq AI for LLM services
- Microsoft for Edge TTS
- OpenAI for Whisper model
- Streamlit team for framework
