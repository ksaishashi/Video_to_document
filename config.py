import os

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRAME_DIR = os.path.join(BASE_DIR, "output", "frames")
AUDIO_PATH = os.path.join(BASE_DIR, "output", "audio.wav")
FINAL_DOCUMENT_PATH = os.path.join(BASE_DIR, "output", "analysis_report.docx")

# Frame extraction rate
FRAME_RATE = 2  # Extract 1 frame per second
OCR_LANGUAGE = "eng"  # OCR language
