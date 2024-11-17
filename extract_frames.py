import cv2
import os

def extract_frames(video_path: str, output_dir: str, frame_rate: int):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    while True:
        success, frame = cap.read()
        if not success:
            break

        if frame_count % int(cap.get(cv2.CAP_PROP_FPS) / frame_rate) == 0:
            frame_path = os.path.join(output_dir, f"frame_{frame_count:04d}.jpg")
            cv2.imwrite(frame_path, frame)
        frame_count += 1
    cap.release()
