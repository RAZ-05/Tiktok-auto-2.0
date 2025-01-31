from video_processor import split_video, extract_audio, download_video
from subtitle_handler import transcribe_audio, add_subtitles  # ✅ Correct: "add_subtitles"
import os

def process_video(input_source, output_dir="output"):
    print("\n=== Starting processing ===")  # Debug line
    if input_source.startswith(("http://", "https://")):
        print("Downloading video...")
        video_path = download_video(input_source)
        if not video_path:
            print("Download failed.")
            return
    else:
        print("Using local file...")
        video_path = input_source
        if not os.path.exists(video_path):
            print("File not found!")
            return

    print("Splitting video into clips...")
    split_video(video_path, output_dir)
    
    print("Processing clips...")
    for clip_name in os.listdir(output_dir):
        if clip_name.endswith(".mp4") and not clip_name.endswith("_subtitled.mp4"):
            clip_path = os.path.join(output_dir, clip_name)
            audio_path = clip_path.replace(".mp4", ".wav")
            
            print(f"Extracting audio from {clip_name}...")
            extract_audio(clip_path, audio_path)
            
            print(f"Generating subtitles for {clip_name}...")
            subtitles = transcribe_audio(audio_path)
            
            output_path = clip_path.replace(".mp4", "_subtitled.mp4")
            add_subtitles(clip_path, subtitles, output_path)
            print(f"Subtitled clip saved: {output_path}")

if __name__ == "__main__":
    print("=== Opus Clip Generator ===")  # Debug line
    user_input = input("Enter YouTube URL or local file path: ")
    process_video(user_input)
    print("=== Done! ===")  # Debug line