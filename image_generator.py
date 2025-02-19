# image_generator.py
import torch
from diffusers import StableDiffusionPipeline

# Load the Stable Diffusion model
model_id = "stabilityai/stable-diffusion-2-1"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)  # Use float32 for CPU
pipe = pipe.to("cpu")  # Move the model to CPU

def generate_image(prompt):
    # Generate an image from the text prompt
    image = pipe(prompt).images[0]
    return image

# Example usage
if __name__ == "__main__":
    prompt = "A futuristic cityscape at sunset"
    image = generate_image(prompt)
    image.save("generated_image.png")
    print("Image saved as generated_image.png")