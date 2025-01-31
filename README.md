# Tiktok-auto-2.0
A Python-based tool to split long videos into short clips with auto-generated subtitles.   Uses OpenAI's Whisper for speech-to-text and FFmpeg/MoviePy for video processing.   Perfect for content creators to repurpose long-form content into social media highlights.   

Project Tree

TIKTOK-AUTO-2.0/                  # Root folder
├── src/                       # Source code
│   ├── video_processor.py     # Split video into clips (uses FFmpeg)
│   ├── subtitle_handler.py    # Transcribe audio & add subtitles (uses Whisper/MoviePy)
│   └── main.py                # Main workflow
├── input/                     # Input videos (user-provided)
├── output/                    # Processed clips with subtitles
├── requirements.txt           # List of dependencies
└── README.md                  # Project documentation