# image_ai.py
import torch
from diffusers import StableDiffusionPipeline, StableDiffusionImg2ImgPipeline
from PIL import Image
import io

# Initialize both pipelines (text-to-image and image-to-image)
model_id = "stabilityai/stable-diffusion-2-1"
device = "cuda" if torch.cuda.is_available() else "cpu"

# Text-to-Image Pipeline
text_to_image_pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)
text_to_image_pipe = text_to_image_pipe.to(device)

# Image-to-Image Pipeline
image_to_image_pipe = StableDiffusionImg2ImgPipeline.from_pretrained(model_id, torch_dtype=torch.float32)
image_to_image_pipe = image_to_image_pipe.to(device)

def generate_text_to_image(prompt):
    # Generate image from text
    image = text_to_image_pipe(prompt).images[0]
    return image

def generate_image_to_image(prompt, init_image, strength=0.75):
    # Convert image to PIL format
    init_image = Image.open(io.BytesIO(init_image)).convert("RGB")
    # Resize to 512x512 (required by Stable Diffusion)
    init_image = init_image.resize((512, 512))
    # Generate modified image
    image = image_to_image_pipe(
        prompt=prompt,
        image=init_image,
        strength=strength,
        guidance_scale=7.5
    ).images[0]
    return image