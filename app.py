# app.py
from flask import Flask, request, jsonify, send_file
from image_generator import generate_image
import io

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate():
    # Get the prompt from the chat
    data = request.json
    prompt = data.get("prompt", "A beautiful landscape")

    # Generate the image
    image = generate_image(prompt)

    # Save the image to a byte stream
    img_io = io.BytesIO()
    image.save(img_io, "PNG")
    img_io.seek(0)

    # Return the image as a response
    return send_file(img_io, mimetype="image/png")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)  # Use port 8080 for Codespaces