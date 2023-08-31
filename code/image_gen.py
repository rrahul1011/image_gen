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
    st.sidebar.markdown("<hr style='border: 2px solid red; width: 100%;'>", unsafe_allow_html=True)
    st.sidebar.image("/Users/rahulkushwaha/Desktop/Image gen/image_gen/code/cropped-Sigmoid_logo_3x.png", use_column_width=True)
    st.sidebar.markdown("<hr style='border: 2px solid red; width: 100%;'>", unsafe_allow_html=True)
    st.sidebar.markdown(
        "## ImageGenie App\n\n"
        "Welcome to ImageGenie, where you can generate vibrant images based on textual descriptions using the DALL-E API."
        "\n\n"
        "### How to Use?\n\n"
        "1. Enter a description in the text area on the left."
        "2. Click the 'Generate Image' button to see the generated image on the right."
        "\n\n"
        "### Limitations\n\n"
        "Please note the following limitations:\n"
        "- The quality of generated images depends on the input description."
        "- Complex or highly specific descriptions may not yield accurate results."
        "\n\n"
        "Feel free to experiment and have fun!"
    )
    st.markdown("<hr style='border: 2px solid red; width: 100%;'>", unsafe_allow_html=True)
    st.markdown(
        "<div style='text-align: center;'>"
        "<h2 style='color: #3366FF;'>🎨 Welcome! I am the ImageGenie! 🧞‍♂️</h2>"
        "<p style='color: #FF5733;'>I generate vibrant images based on your textual descriptions using the DALL-E API.</p>"
        "</div>",
        unsafe_allow_html=True
    )
    
    st.markdown("<p style='color: #3366FF; font-size: 18px; text-align: center;'>Ask & Visualize 🖼️</p>", unsafe_allow_html=True)
    
    # Apply CSS to style the horizontal lines
    st.markdown("<hr style='border: 2px solid red; width: 100%;'>", unsafe_allow_html=True)
    
    user_input = st.text_area("Enter a Description", "")

    if st.button("Generate Image"):
        if user_input:
            st.info("Generating image...")
            payload = {
                "inputs": user_input,
            }
            image_bytes = query(payload)
            image = Image.open(io.BytesIO(image_bytes))
            st.image(image, caption="Generated Image", use_column_width=True)
            st.success("Image generated successfully!")
        else:
            st.warning("Please enter a text prompt.")

if __name__ == "__main__":
    main()
