
# from pyannote.audio import Pipeline

# def diarize_audio(audio_path: str, transcription: dict) -> list:
#     """Perform speaker diarization."""
#     pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization@2.1", use_auth_token="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")
#     diarization = pipeline(audio_path)
#     diarized_segments = []
#     for segment, _, speaker in diarization.itertracks(yield_label=True):
#         diarized_segments.append({
#             "speaker": speaker,
#             "start": segment.start,
#             "end": segment.end,
#             "text": transcription["text"]  # Timestamp alignment can be improved
#         })
#     return diarized_segments

from pyannote.audio import Pipeline

def diarize_audio(audio_path: str, transcription: dict) -> list:
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization@2.1", use_auth_token="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")
    diarization = pipeline(audio_path,num_speakers=4)

    diarized_segments = []
    for segment, _, speaker in diarization.itertracks(yield_label=True):
        text = " ".join(
            word["text"]
            for word in transcription["segments"]
            if segment.start <= word["start"] <= segment.end
        )
        diarized_segments.append({
            "speaker": speaker,
            "start": segment.start,
            "end": segment.end,
            "text": text,
        })
    return diarized_segments

