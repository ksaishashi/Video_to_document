import os
from config import FRAME_DIR, AUDIO_PATH, FINAL_DOCUMENT_PATH, FRAME_RATE
from extract_frames import extract_frames
from extract_audio import extract_audio
from describe_frames import process_frame_descriptions
from extract_text import process_frame_text
from transcribe_audio import transcribe_audio, align_speech_to_frames
from diarize_speakers import diarize_audio
from deduplicate_frames import deduplicate_frames
from generate_document import create_document

def main(video_path: str):
    os.makedirs(FRAME_DIR, exist_ok=True)

    print("[INFO] Extracting frames...")
    extract_frames(video_path, FRAME_DIR, FRAME_RATE)

    print("[INFO] Deduplicating frames...")
    unique_frames = deduplicate_frames(FRAME_DIR)

    print("[INFO] Extracting audio...")
    extract_audio(video_path, AUDIO_PATH)

    print("[INFO] Generating frame descriptions...")
    frame_descriptions = process_frame_descriptions(unique_frames)

    print("[INFO] Extracting text from frames...")
    frame_texts = process_frame_text(unique_frames)

    print("[INFO] Transcribing audio...")
    transcription = transcribe_audio(AUDIO_PATH)

    print("[INFO] Aligning speech to frames...")
    frame_times = [(idx / FRAME_RATE, (idx + 1) / FRAME_RATE) for idx in range(len(unique_frames))]
    aligned_speech = align_speech_to_frames(transcription, frame_times)

    print("[INFO] Performing speaker diarization...")
    diarized_transcription = diarize_audio(AUDIO_PATH, transcription)

    print("[INFO] Creating final document...")
    create_document(FINAL_DOCUMENT_PATH, frame_descriptions, frame_texts, diarized_transcription, aligned_speech, unique_frames)

    print(f"[SUCCESS] Document created at {FINAL_DOCUMENT_PATH}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Video to Document Pipeline")
    parser.add_argument("video_path", type=str, help="Path to the input video file")
    args = parser.parse_args()
    main(args.video_path)
