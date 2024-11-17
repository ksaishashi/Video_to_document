import whisper

def transcribe_audio(audio_path: str) -> dict:
    """Transcribe audio with word-level timestamps using Whisper."""
    model = whisper.load_model("base")
    result = model.transcribe(audio_path, word_timestamps=True)
    return result

def align_speech_to_frames(transcription, frame_times):
    """Align transcribed text to frames based on timestamps."""
    aligned_text = {frame_time: "" for frame_time in frame_times}
    for word in transcription['segments']:
        for frame_time in frame_times:
            if frame_time[0] <= word['start'] <= frame_time[1]:
                aligned_text[frame_time] += word['text'] + " "
    return aligned_text
