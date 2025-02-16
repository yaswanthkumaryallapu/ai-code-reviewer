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
        "Review the following code, identify errors, suggest fixes, and provide a simplified version:\n\n"
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

        body {
            background-color:rgb(255, 173, 90);
            color: #FFFFFF;
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
            background-color: #1E1E1E;
            color:rgb(253, 235, 94);
        }
        
        .stTextArea textarea {
            background-color: #333;
            color: white;
            border-radius: 10px;
        }

        .stButton button {
            background-color: #FF4B4B;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            transition: 0.3s;
        }

        .stButton button:hover {
            background-color: #FF3333;
        }
        
    </style>
    """,
    unsafe_allow_html=True
)

# **Header Layout: Left Title + Right Banner Image**
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

# **User Input for Code Review**
st.subheader("📜 Paste Your Code Below:")
code_snippet = st.text_area("Enter your code here...", height=200)

# **Review Button**
if st.button("🚀 Review Code"):
    if code_snippet.strip():
        st.write("⏳ Analyzing your code, please wait...")
        time.sleep(1)  # Simulating a loading effect

        result = review_code(code_snippet)
        
        # **Display AI Response in Styled Box**
        st.markdown(f"<div class='review-container'><b>📝 Review Result:</b><br><br>{result}</div>", unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter some code before submitting.")

