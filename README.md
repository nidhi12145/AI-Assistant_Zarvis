# 🤖 AI-Assistant Zarvis

A Python-based voice assistant inspired by **Jarvis** from Iron Man.  
Zarvis can understand your voice commands, respond intelligently using AI (OpenAI), fetch news, play music, and open websites — just like a personal assistant.

---

## ✨ Features
- 🎤 **Voice Recognition** – Listens to commands using your microphone.  
- 🗣 **Text-to-Speech (TTS)** – Responds back with a natural voice (Google TTS + PyGame).  
- 🤖 **AI Responses** – Uses OpenAI's GPT model to answer queries and general tasks.  
- 🌐 **Web Control** – Open sites like Google, YouTube, Facebook, LinkedIn via voice.  
- 📰 **Latest News** – Fetches top news headlines via the News API.  
- 🎶 **Music Playback** – Plays pre-defined songs from `musicLibrary.py`.  

---


## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/<username>/AI-Assistant_Zarvis.git
cd AI-Assistant_Zarvis
```
### 2. Install Dependencies
Make sure you have Python 3.8+ installed. Then run:
```bash
pip install -r requirements.txt
```
If requirements.txt is not present, install manually:
```bash
pip install speechrecognition pyttsx3 openai gtts pygame requests
```
Also, install PyAudio (required for microphone input):

On Windows:
```bash
pip install pipwin
pipwin install pyaudio
```

On Linux/macOS:
```bash
brew install portaudio  # macOS
sudo apt-get install portaudio19-dev python3-pyaudio  # Linux
pip install pyaudio
```

3. Add API Keys
This project uses:
OpenAI API Key (for AI responses)
NewsAPI Key (for fetching news)

Replace the placeholders in main.py and client.py:
```bash
api_key="your_openai_api_key"
newsapi="your_newsapi_key"
```
🎮 Usage

Run the assistant with:
```bash
python main.py
```

Say "Jarvis" to activate.

Then give a command, for example:

"Open Google" → Opens Google in browser

"Play Soulmate" → Plays the song from musicLibrary.py

"News" → Reads top headlines aloud

"What is Python?" → AI-generated answer

🔮 Future Improvements
Add GUI interface
Support for more APIs (weather, reminders, calendar)
Smarter conversation memory
Custom wake word
