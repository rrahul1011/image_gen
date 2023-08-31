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
    st.title("Visualize your imagination")
    st.markdown("---")

    user_input = st.text_input("Enter a your thought !", "")

    if st.button("Generate"):
        if user_input:
            image_bytes = query({"inputs": user_input,
                            })
            image = Image.open(io.BytesIO(image_bytes))
            st.image(image)
        else:
            st.warning("Please enter a text prompt.")



if __name__ == "__main__":
    main()


