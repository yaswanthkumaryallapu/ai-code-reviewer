import os
import streamlit as st
import google.generativeai as genai
import time

# Set Gemini API Key (Replace with your actual key)
GEMINI_API_KEY = "AIzaSyAhz0YH_o4gaSSkC0L1Szib2N59tPzBUsE"
genai.configure(api_key=GEMINI_API_KEY)

# Function to review code using Gemini AI
def review_code(code_snippet):
    prompt = (
        "Review the following code line by line and give error if there and suggest the simplest code for the given code :\n\n"
        f"{code_snippet}"
    )
    
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text if response else "No response from AI."
    
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Streamlit Page Configuration
st.set_page_config(page_title="AI Code Reviewer", page_icon="🔍", layout="wide")

# **Custom CSS for UI Enhancements & Animations**
st.markdown(
    """
    <style>
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            width: 100%;
            padding: 20px;
        }

        .title {
            flex: 1;
            text-align: left;
            animation: fadeIn 1s ease-in-out;
        }

        .banner {
            flex: 1;
            text-align: right;
            animation: fadeIn 1.5s ease-in-out;
        }

        .review-container {
            animation: fadeIn 1s ease-in-out;
            border-radius: 12px;
            padding: 15px;
            background-color: #f8f9fa;
            box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
        }

        .stTextArea > label {
            font-size: 18px;
            font-weight: bold;
        }

        .stButton > button {
            background-color: #007bff !important;
            color: white !important;
            border-radius: 8px;
            font-size: 16px;
            padding: 8px 20px;
            transition: 0.3s;
        }

        .stButton > button:hover {
            background-color: #0056b3 !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# **Title & Banner**
st.markdown(
    """
    <div class="container">
        <div class="title">
            <h1>🔍 AI Code Reviewer</h1>
            <h4 style="color: gray;">Get AI-powered code review and suggestions instantly.</h4>
        </div>
        <div class="banner">
            <img src="https://cdn.prod.website-files.com/6751b9c40053fbf4219732d4/6785268fc609f619d0cddf4a_Generative-AI-for-Code-1-e1695724469521.jpeg" width="400">
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
st.write("---")

# **Code Input**
code_input = st.text_area("📜 Paste Your Code Below:", height=200)

# **Submit Button with Loading Effect**
if st.button("🚀 Review Code"):
    with st.spinner("🔍 AI is reviewing your code..."):
        time.sleep(2)  # Simulate processing time
        review_result = review_code(code_input)

    # **Show Review Results**
    st.markdown(
        f"""
        <div class="review-container">
            <h3>✅ AI Code Review:</h3>
            <pre>{review_result}</pre>
        </div>
        """,
        unsafe_allow_html=True
    )
