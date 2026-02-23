# 🎬 AutoShorts — AI-Powered YouTube Shorts / TikTok Generator

Automatically transform any video into a viral short-form clip using AI-generated commentary, neural text-to-speech, and auto-synced subtitles.

---

## 🚀 Pipeline

```
Video → AI Script (Groq) → TTS (Edge TTS) → Transcribe TTS (Whisper) → Edit & Export
```

1. **Script Generation** — Groq (LLaMA 3.3) writes a punchy TikTok-style voiceover script
2. **Text to Speech** — Microsoft Edge TTS converts the script to natural neural audio
3. **Transcription** — Whisper transcribes the TTS audio so subtitles sync perfectly to the voice
4. **Video Editing** — MoviePy crops to vertical (1080×1920), overlays subtitles, adds title, and composites audio

---

## 📁 Project Structure

```
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
```

---

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/AutoShorts.git
cd AutoShorts
pip install -r requirements.txt
```

### requirements.txt

```
groq
edge-tts
openai-whisper
moviepy
python-dotenv
```

> **Note:** Whisper also requires [ffmpeg](https://ffmpeg.org/download.html) to be installed on your system.

---

## 🔑 Environment Setup

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your-groq-api-key
```

Get your free Groq API key at [console.groq.com](https://console.groq.com)

---

## 🧩 Modules

### `ScriptGenerator` — `script_generator.py`

Generates a structured TikTok-style voiceover script using Groq's LLaMA model.

**Script structure:**
- **Hook** — Grabs attention in 1-2 sentences
- **Body** — Explains the video briefly and fast
- **Outro** — Call to action or punchline

```python
from script_generator import ScriptGenerator

generator = ScriptGenerator()  # picks up GROQ_API_KEY from .env
script = generator.generate(
    topic="A man breaks the world record for fastest 100m sprint",
    style="dramatic and intense"
)
```

**Available styles:** `energetic`, `funny and sarcastic`, `dramatic and intense`, `educational and calm` — or any custom style string.

---

### `TTSEngine` — `tts_engine.py`

Converts the script to natural-sounding neural audio using Microsoft Edge TTS (free, no API key required).

```python
from tts_engine import TTSEngine

tts = TTSEngine(voice='uk_male', rate='+10%')
audio_path = tts.synthesize(script, output_path='output/audio/commentary.mp3')
```

**Built-in voices:**

| Key | Voice |
|-----|-------|
| `us_male` | en-US-GuyNeural |
| `us_female` | en-US-JennyNeural |
| `uk_male` | en-GB-RyanNeural |
| `uk_female` | en-GB-SoniaNeural |
| `au_male` | en-AU-WilliamNeural |
| `india_male` | en-IN-PrabhatNeural |

> Run `TTSEngine.list_voices()` to browse all 400+ available voices.

---

### `Transcriber` — `transcriber.py`

Transcribes the TTS audio file using OpenAI Whisper, producing timestamped subtitle segments that are perfectly synced to the commentary voice.

```python
from transcriber import Transcriber

transcriber = Transcriber(model_size='base')
subtitles = transcriber.transcribe('output/audio/commentary.mp3')
# Returns: [{'text': '...', 'start': 0.0, 'end': 2.5}, ...]
```

**Whisper model sizes:**

| Model | Speed | Accuracy |
|-------|-------|----------|
| `tiny` | Fastest | Lower |
| `base` | Fast | Good ✅ |
| `small` | Medium | Better |
| `medium` | Slow | Best |

---

### `VideoEditor` — `video_editor.py`

Handles all video processing — cropping to vertical format, adding title, overlaying subtitles, and compositing audio.

```python
from video_editor import VideoEditor

editor = (
    VideoEditor('MyVideo.mp4')
    .load_subtitles(subtitles)
    .load_commentary('output/audio/commentary.mp3')
)
editor.render()
```

**What it does:**
- Crops landscape video to **1080×1920** (vertical/Shorts format)
- Adds a **3-second title card** at the start
- Overlays **auto-synced subtitles** at the bottom
- Replaces original audio with the **AI commentary**

---

## ▶️ Usage

### Full Pipeline

```python
from pipeline import ShortsPipeline

pipeline = ShortsPipeline()

pipeline.run(
    video_path='MyVideo.mp4',
    topic='Top 5 insane moments from this clip',
    commentary_style='funny and sarcastic'
)
```

### Step by Step

```python
from script_generator import ScriptGenerator
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
```

---

## 🛠️ Configuration

| Parameter | Default | Description |
|-----------|---------|-------------|
| `voice` | `us_male` | TTS voice accent |
| `rate` | `+0%` | Speech speed (`+20%` faster, `-20%` slower) |
| `pitch` | `+0Hz` | Voice pitch |
| `model_size` | `base` | Whisper model size |
| `font` | `Chunk Five Print.otf` | Subtitle font |
| `output_size` | `1080x1920` | Output video resolution |

---

## 📦 Tech Stack

| Tool | Purpose | Cost |
|------|---------|------|
| [Groq](https://groq.com) | LLaMA 3.3 script generation | Free tier |
| [Edge TTS](https://github.com/rany2/edge-tts) | Neural text to speech | Free |
| [OpenAI Whisper](https://github.com/openai/whisper) | Audio transcription | Free (local) |
| [MoviePy](https://zulko.github.io/moviepy/) | Video editing | Free |

---

## 🗺️ Roadmap

- [ ] Batch processing for multiple videos
- [ ] CLI interface
- [ ] Background music support
- [ ] Auto-upload to YouTube / TikTok
- [ ] Web UI

---

## 📄 License

MIT License — feel free to use, modify, and distribute.
