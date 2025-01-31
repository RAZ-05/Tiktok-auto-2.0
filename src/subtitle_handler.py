from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import whisper

def transcribe_audio(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result["segments"]

def add_subtitles(video_path, subtitles, output_path):
    video = VideoFileClip(video_path)
    clips = [video]  # Original video clip
    
    for sub in subtitles:
        # Create subtitle text clip
        txt_clip = (
            TextClip(
                sub["text"],
                fontsize=24,
                color="white",
                bg_color="rgba(0,0,0,0.5)",
                size=(video.w * 0.8, None)
            )
            .set_position(("center", "bottom"))
            .set_start(sub["start"])
            .set_duration(sub["end"] - sub["start"])
        )
        clips.append(txt_clip)
    
    # Combine all clips and render
    final_video = CompositeVideoClip(clips)
    final_video.write_videofile(output_path)  # Fixed syntax (use parentheses)