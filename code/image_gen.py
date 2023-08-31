import streamlit as st
import requests
import io
from PIL import Image

API_URL = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
API_TOKEN = "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"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

def main():
    st.title("Image Generation from Text Prompt")

    st.write("Enter a text prompt:")
    user_input = st.text_area("", "")

    if st.button("Generate Image"):
        if user_input:
            payload = {
                "inputs": user_input,
            }
            image_bytes = query(payload)
            image = Image.open(io.BytesIO(image_bytes))
            st.image(image, caption="Generated Image", use_column_width=True)
        else:
            st.warning("Please enter a text prompt.")

if __name__ == "__main__":
    main()
