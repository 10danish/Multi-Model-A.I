from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai 
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(input,image):
    if input!="":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response

st.set_page_config(page_title="Gemini-vision mock model")
st.header("Image-text A.I")
input=st.text_input("Input:",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
        # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    image = Image.open(uploaded_file)

submit=st.button("Submit for info on image.")
if submit:
    response=get_gemini_response(input,image)
    st.subheader("The Response is:\n")
    # for chunk in response:
    st.code(response.text)
 