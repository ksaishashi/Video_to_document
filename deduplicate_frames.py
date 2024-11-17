import cv2
import os

def deduplicate_frames(frame_dir: str, threshold: float = 0.8) -> list:
    """Deduplicate frames using histogram comparison."""
    unique_frames = []
    prev_hist = None

    for frame_file in sorted(os.listdir(frame_dir)):
        frame_path = os.path.join(frame_dir, frame_file)
        frame = cv2.imread(frame_path)

        # Compute histogram
        hist = cv2.calcHist([frame], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
        hist = cv2.normalize(hist, hist).flatten()

        if prev_hist is not None:
            similarity = cv2.compareHist(prev_hist, hist, cv2.HISTCMP_CORREL)
            if similarity > threshold:
                continue  # Skip duplicate frames

        unique_frames.append(frame_path)
        prev_hist = hist

    return unique_frames
