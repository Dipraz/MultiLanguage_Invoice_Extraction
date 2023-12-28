# Q&A Chatbot
#from langchain.llms import OpenAI


from dotenv import load_dotenv

load_dotenv() ## load all the environment variables from the .env file

import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image

import google.generativeai as genai

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##Function to load Gemini Pro Vision model and get responses.

def get_gemini_response(input,image,prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input,image[0],prompt])
    return response.text


def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
    
#initialize the Streamlit app

st.set_page_config(page_title="MultiLanguage Invoice Extraction")

st.header("Invoice Image Analysis")
input = st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Please Choose Your Invoice image...", type=["jpg", "jpeg","png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Your Uploaded Image.", use_column_width=True)
    
    
    
submit=st.button("Tell me everything about the invoice image")

input_prompt = """
                Prompt:
                Your expertise in invoice comprehension is unparalleled. You've meticulously analyzed countless invoices, deciphering their intricacies across industries, languages, and formats. Now, a new challenge awaits: extracting precise insights from invoice images.
                Your mission:
                Immerse yourself in each invoice image. Engage your visual perception and knowledge to meticulously scan every detail, from headers and line items to fine print and logos.
                Grasp the invoice's essence. Discern the vendor, purchaser, date, payment terms, products or services rendered, total amounts, and any other pertinent information.
                Answer questions with unwavering accuracy. Anticipate inquiries regarding invoice amounts, due dates, specific line items, tax details, vendor information, payment status, or any other relevant aspect.
                Communicate with clarity and precision. Present your findings in a concise, informative, and easily understandable manner, ensuring users have the insights they need.
                Unleash your expertise. Embrace the challenge. Become the ultimate invoice interpreter.   
                """

        
## If submit button is clicked

if submit:
    image_data = input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("The Response is...")
    st.write(response)
else:
    st.warning("Please upload an image before analyzing")