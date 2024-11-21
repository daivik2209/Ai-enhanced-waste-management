import streamlit as st
import requests

# Backend URL
BACKEND_URL = "http://127.0.0.1:5000/classify-waste"

# Set page configuration
st.set_page_config(page_title="AI-Enhanced Waste Management", page_icon="♻️", layout="centered")

# Apply custom CSS styling for buttons, file uploader, and footer
st.markdown("""
    <style>
        .stApp {
            font-family: 'Arial', sans-serif;
        }
        .stTitle {
            text-align: center;
            font-size: 3rem;
            color: white; /* White color for title */
            margin-top: 30px;
            font-weight: bold;
        }
        .stWrite {
            text-align: center;
            font-size: 1.2rem;
            color: #7f8c8d; /* Light gray color for description */
        }
        .stButton button {
            background-color: #3498db;
            color: white;
            border-radius: 25px;
            padding: 10px 30px;
            font-size: 1.2rem;
            border: none;
            transition: background-color 0.3s;
        }
        .stButton button:hover {
            background-color: #2980b9;
        }
        .stFileUploader input[type="file"] {
            color: black; /* Set the text color to black for file upload button */
            background-color: #ecf0f1; /* Optional: make background light gray */
            border: 2px solid #3498db;
            padding: 10px 20px;
            border-radius: 5px;
            font-size: 1rem;
        }
        .stImage {
            display: block;
            margin: 20px auto;
            border-radius: 10px;
        }
        .stSuccess, .stError {
            text-align: center;
            font-size: 1.5rem;
            margin-top: 20px;
        }
        .footer {
            background-color: #ecf0f1;
            color: #2c3e50;
            text-align: center;
            padding: 20px;
            font-size: 1rem;
            border-radius: 10px;
            margin-top: 40px;
        }
        .footer a {
            color: #3498db;
            text-decoration: none;
            font-weight: bold;
        }
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.markdown('<div class="stTitle">AI-Enhanced Waste Management System ♻️</div>', unsafe_allow_html=True)
st.markdown('<div class="stWrite">Upload an image of waste to classify its type using AI!</div>', unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"], key="file_uploader")

if uploaded_file:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True, class_="stImage")

    # Button to trigger classification
    if st.button("Classify Waste", key="classify_button"):
        with st.spinner("Classifying... Please wait!"):
            # Prepare file for backend
            files = {'file': uploaded_file.getvalue()}
            response = requests.post(BACKEND_URL, files=files)
            
            if response.status_code == 200:
                waste_type = response.json()['waste_type']
                st.success(f"Waste type: {waste_type}", icon="✅")
            else:
                st.error("Error in waste classification. Please try again.", icon="❌")
else:
    st.info("Please upload an image of waste to classify its type.", icon="ℹ️")

# Footer with attractive design and links
st.markdown("""
    <div class="footer">
        <p>Made with ❤️ by [Your Name](#) | AI Waste Management System</p>
        <p>Check out our <a href="https://www.example.com" target="_blank">Project Documentation</a></p>
    </div>
""", unsafe_allow_html=True)