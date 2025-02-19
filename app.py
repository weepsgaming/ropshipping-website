# app.py
from flask import Flask, request, jsonify, send_file
from image_ai import generate_text_to_image, generate_image_to_image
import io

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Image Generator is running! Use /generate or /modify endpoints."

@app.route("/generate", methods=["POST"])
def generate():
    # Generate image from text
    data = request.json
    prompt = data.get("prompt", "A futuristic cityscape")
    image = generate_text_to_image(prompt)
    img_io = io.BytesIO()
    image.save(img_io, "PNG")
    img_io.seek(0)
    return send_file(img_io, mimetype="image/png")

@app.route("/modify", methods=["POST"])
def modify():
    # Modify an existing image using a prompt
    prompt = request.form.get("prompt", "Add a rainbow to the sky")
    init_image = request.files["image"].read()  # Uploaded image
    strength = float(request.form.get("strength", 0.75))
    image = generate_image_to_image(prompt, init_image, strength)
    img_io = io.BytesIO()
    image.save(img_io, "PNG")
    img_io.seek(0)
    return send_file(img_io, mimetype="image/png")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)