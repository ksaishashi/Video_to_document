import ffmpeg
import os

def extract_audio(video_path: str, output_audio_path: str):
    os.makedirs(os.path.dirname(output_audio_path), exist_ok=True)
    ffmpeg.input(video_path).output(output_audio_path).run(overwrite_output=True)
