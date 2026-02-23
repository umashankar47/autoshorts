🎬 AutoShorts — AI-Powered YouTube Shorts / TikTok Generator
Automatically transform any video into a viral short-form clip using AI-generated commentary, neural text-to-speech, and auto-synced subtitles.

🚀 Pipeline
Video → AI Script (Groq) → TTS (Edge TTS) → Transcribe TTS (Whisper) → Edit & Export

Script Generation — Groq (LLaMA 3.3) writes a punchy TikTok-style voiceover script
Text to Speech — Microsoft Edge TTS converts the script to natural neural audio
Transcription — Whisper transcribes the TTS audio so subtitles sync perfectly to the voice
Video Editing — MoviePy crops to vertical (1080×1920), overlays subtitles, adds title, and composites audio


📁 Project Structure
AutoShorts/
│
├── script_generator.py   # Groq-powered TikTok script writer
├── tts_engine.py         # Edge TTS audio synthesis
├── transcriber.py        # Whisper-based TTS transcription
├── video_editor.py       # MoviePy video editing & export
├── pipeline.py           # Orchestrates the full pipeline
│
├── output/
│   └── audio/            # Generated commentary audio
│
├── .env                  # API keys (never commit this)
└── requirements.txt

⚙️ Installation
bashgit clone https://github.com/yourusername/AutoShorts.git
cd AutoShorts
pip install -r requirements.txt
requirements.txt
groq
edge-tts
openai-whisper
moviepy
python-dotenv

Note: Whisper also requires ffmpeg to be installed on your system.


🔑 Environment Setup
Create a .env file in the root directory:
GROQ_API_KEY=your-groq-api-key
Get your free Groq API key at console.groq.com

🧩 Modules
ScriptGenerator — script_generator.py
Generates a structured TikTok-style voiceover script using Groq's LLaMA model.
Script structure:

Hook — Grabs attention in 1-2 sentences
Body — Explains the video briefly and fast
Outro — Call to action or punchline

pythonfrom script_generator import ScriptGenerator

generator = ScriptGenerator()  # picks up GROQ_API_KEY from .env
script = generator.generate(
    topic="A man breaks the world record for fastest 100m sprint",
    style="dramatic and intense"
)
Available styles: energetic, funny and sarcastic, dramatic and intense, educational and calm — or any custom style string.

TTSEngine — tts_engine.py
Converts the script to natural-sounding neural audio using Microsoft Edge TTS (free, no API key required).
pythonfrom tts_engine import TTSEngine

tts = TTSEngine(voice='uk_male', rate='+10%')
audio_path = tts.synthesize(script, output_path='output/audio/commentary.mp3')
Built-in voices:
KeyVoiceus_maleen-US-GuyNeuralus_femaleen-US-JennyNeuraluk_maleen-GB-RyanNeuraluk_femaleen-GB-SoniaNeuralau_maleen-AU-WilliamNeuralindia_maleen-IN-PrabhatNeural

Run TTSEngine.list_voices() to browse all 400+ available voices.


Transcriber — transcriber.py
Transcribes the TTS audio file using OpenAI Whisper, producing timestamped subtitle segments that are perfectly synced to the commentary voice.
pythonfrom transcriber import Transcriber

transcriber = Transcriber(model_size='base')
subtitles = transcriber.transcribe('output/audio/commentary.mp3')
# Returns: [{'text': '...', 'start': 0.0, 'end': 2.5}, ...]
Whisper model sizes:
ModelSpeedAccuracytinyFastestLowerbaseFastGood ✅smallMediumBettermediumSlowBest

VideoEditor — video_editor.py
Handles all video processing — cropping to vertical format, adding title, overlaying subtitles, and compositing audio.
pythonfrom video_editor import VideoEditor

editor = (
    VideoEditor('MyVideo.mp4')
    .load_subtitles(subtitles)
    .load_commentary('output/audio/commentary.mp3')
)
editor.render()
What it does:

Crops landscape video to 1080×1920 (vertical/Shorts format)
Adds a 3-second title card at the start
Overlays auto-synced subtitles at the bottom
Replaces original audio with the AI commentary


▶️ Usage
Full Pipeline
pythonfrom pipeline import ShortsPipeline

pipeline = ShortsPipeline()

pipeline.run(
    video_path='MyVideo.mp4',
    topic='Top 5 insane moments from this clip',
    commentary_style='funny and sarcastic'
)
Step by Step
pythonfrom script_generator import ScriptGenerator
from tts_engine import TTSEngine
from transcriber import Transcriber
from video_editor import VideoEditor

# 1. Generate script
script = ScriptGenerator().generate(topic="...", style="energetic")

# 2. Convert to audio
audio_path = TTSEngine(voice='uk_male').synthesize(script)

# 3. Transcribe TTS for subtitle sync
subtitles = Transcriber().transcribe(audio_path)

# 4. Edit and export
VideoEditor('MyVideo.mp4').load_subtitles(subtitles).load_commentary(audio_path).render()

🛠️ Configuration
ParameterDefaultDescriptionvoiceus_maleTTS voice accentrate+0%Speech speed (+20% faster, -20% slower)pitch+0HzVoice pitchmodel_sizebaseWhisper model sizefontChunk Five Print.otfSubtitle fontoutput_size1080x1920Output video resolution

📦 Tech Stack
ToolPurposeCostGroqLLaMA 3.3 script generationFree tierEdge TTSNeural text to speechFreeOpenAI WhisperAudio transcriptionFree (local)MoviePyVideo editingFree

🗺️ Roadmap

 Batch processing for multiple videos
 CLI interface
 Background music support
 Auto-upload to YouTube / TikTok
 Web UI


📄 License
MIT License — feel free to use, modify, and distribute.
