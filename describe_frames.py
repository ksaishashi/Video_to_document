from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import os

def process_frame_descriptions(frame_paths: list) -> dict:
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    descriptions = {}
    for frame_path in frame_paths:
        image = Image.open(frame_path)
        inputs = processor(image, return_tensors="pt")
        outputs = model.generate(**inputs)
        description = processor.decode(outputs[0], skip_special_tokens=True)
        descriptions[os.path.basename(frame_path)] = description
    return descriptions
