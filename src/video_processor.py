import ffmpeg  # Fixed typo (not f:mpeg)
import os
from pytube import YouTube

# Function to download video from URL
def download_video(url, output_dir='input'):
    try:
        os.makedirs(output_dir, exist_ok=True)
        yt = YouTube(url)
        stream = yt.streams.filter(
            progressive=True, 
            file_extension="mp4"
        ).order_by('resolution').desc().first()
        output_path = os.path.join(output_dir, 'downloaded_video.mp4')
        stream.download(output_path=output_path)
        return output_path
    except Exception as e:
        print(f"Error downloading video: {e}")  # Fixed f-string
        return None

def split_video(input_path, output_dir, clip_duration=60):
    os.makedirs(output_dir, exist_ok=True)
    probe = ffmpeg.probe(input_path)
    duration = float(probe['format']['duration'])
    
    for start_time in range(0, int(duration), clip_duration):
        end_time = min(start_time + clip_duration, duration)
        output_path = os.path.join(output_dir, f"clip_{start_time}.mp4")
        (
            ffmpeg.input(input_path, ss=start_time, to=end_time)
            .output(output_path)
            .run()
        )

def extract_audio(video_path, audio_path):
    (
        ffmpeg.input(video_path)
        .output(audio_path, acodec='pcm_s16le')
        .run()
    )