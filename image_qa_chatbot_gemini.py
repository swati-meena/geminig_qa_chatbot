from dotenv import load_dotenv
import streamlit as st
from PIL import Image
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Generative AI
genai.configure(api_key="AIzaSyAbKj0FiFGq0GAftFvcmpDlaycxX7RNP9s")

# Function to load OpenAI model and get responses
def get_gemini_response(input, image):
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

# Initialize Streamlit app
st.set_page_config(page_title="Gemini Image Demo")

# Add a background image using CSS
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://media.gettyimages.com/id/2156749469/video/artificial-intelligence-robots.jpg?s=640x640&k=20&c=-BncP9k65rqVNd5E5VjX6zDVfxiUSBbYr1WviEgpogk=");
    background-size: 100%;
    background-repeat: no-repeat;
    color:white;
}
[data-testid="stHeader"] {
    background: rgba(0, 0, 0, 0); /* Make header transparent */
}
[data-testid="stVerticalBlock"]{
    margin-left:50%;
    width: 50%; /* Increase the width to make it longer */

}
label {
    color: white !important;
}
[data-testid="stBaseButton-secondary"]{
    background-color:red;
    color:white;
}
[data-testid="stBaseButton-secondary"]:hover {
    background-color: red;
    color: white;
}

</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Header and input
st.header("Q&A Image Chatbot")
input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.")

submit = st.button("Tell me about the image")

# Generate response on submit
if submit:
    response = get_gemini_response(input, image)
    st.subheader("The Response is")
    st.write(response)
