import cv2
import pytesseract
from PIL import Image
import os

def preprocess_image(image_path):
    """Preprocess the image for better OCR accuracy."""
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Resize for better text detection
    image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
    # Apply thresholding
    _, image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return image

def process_frame_text(frame_paths: list) -> dict:
    """Extract text from frames using OCR with pre-processing."""
    texts = {}
    for frame_path in frame_paths:
        processed_image = preprocess_image(frame_path)
        text = pytesseract.image_to_string(processed_image)
        texts[os.path.basename(frame_path)] = text.strip()
    return texts
