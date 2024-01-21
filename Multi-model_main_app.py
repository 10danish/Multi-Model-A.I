from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai 
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model1=genai.GenerativeModel("gemini-pro")
model2=genai.GenerativeModel("gemini-pro-vision")
def get_gemini_M1(input):
    response=model1.generate_content(input)
    return response

def get_gemini_M2(input,image):
    if input!="":
        response=model2.generate_content([input,image])
    else:
        response=model2.generate_content(image)
    return response

st.set_page_config(layout="wide")
#you can add your logo image here.
#st.image("logo.png", width=150) 
st.header("Multi-Model A.I")

    
main_container = st.container()
with main_container:
    col1, col2 = st.columns((2,2))

    with col1:
        # Add chart #1
     input1=st.text_input("Input:",key="input1")
     submit=st.button("Submit for text only.")
     if submit:
        resp1=get_gemini_M1(input1)
        st.subheader("The Response is:\n")
        # for chunk in response:
        st.write(resp1.text)


    with col2:
        # b1 = st.button("click to upload pic")
        # if b1:
            input2 = st.text_input("Input for image:", key="input2")
            uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

            if uploaded_file is not None:
                # Display the uploaded image
                st.image(uploaded_file, caption="Uploaded Image", width=300)
                image = Image.open(uploaded_file)

                submit = st.button("Submit for info on image.")
                if submit:
                    resp2 = get_gemini_M2(input2, image)
                    st.subheader("The Response is:\n")
                    st.code(resp2.text)
