AutoShorts — AI-Powered YouTube Shorts / TikTok Generator
Automatically transform any video into a viral short-form clip using AI-generated commentary, neural text-to-speech, and auto-synced subtitles.

Pipeline
Video → AI Script (Groq) → TTS (Edge TTS) → Transcribe TTS (Whisper) → Edit & Export

Script Generation — Groq (LLaMA 3.3) writes a punchy TikTok-style voiceover script
Text to Speech — Microsoft Edge TTS converts the script to natural neural audio
Transcription — Whisper transcribes the TTS audio so subtitles sync perfectly to the voice
Video Editing — MoviePy crops to vertical (1080×1920), overlays subtitles, adds title, and composites audio


Project Structure
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


Environment Setup
Create a .env file in the root directory:

GROQ_API_KEY=your-groq-api-key


Modules
ScriptGenerator — script_generator.py
Generates a structured TikTok-style voiceover script using Groq's LLaMA model.
Script structure:

Hook — Grabs attention in 1-2 sentences
Body — Explains the video briefly and fast
Outro — Call to action or punchline



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

Crops landscape video to 1080×1920 (vertical/Shorts format)
Adds a 3-second title card at the start
Overlays auto-synced subtitles at the bottom
Replaces original audio with the AI commentary



🗺️ Roadmap

 Batch processing for multiple videos
 CLI interface
 Background music support
 Auto-upload to YouTube / TikTok
 Web UI


📄 License
MIT License — feel free to use, modify, and distribute.
