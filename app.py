import os
import streamlit as st
import google.generativeai as genai

# Set Gemini API Key (Replace with your actual key)
os.environ["GEMINI_API_KEY"] = "AIzaSyAhz0YH_o4gaSSkC0L1Szib2N59tPzBUsE"
genai.configure(api_key=os.environ["GEMINI_API_KEY"])


def review_code(code_snippet):
    """Calls Gemini AI model to review the provided code."""
    prompt = f"Review the following code and suggest improvements:\n\n{code_snippet}"

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)

        return response.text if response else "No response from AI."
    
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit Page Configuration
st.set_page_config(page_title="AI Code Reviewer", layout="wide")

# **Flexbox for Layout: Left-Aligned Text & Right-Aligned Image**
st.markdown(
    """
    <div style="display: flex; align-items: center; justify-content: space-between;">
        <div style="flex: 1; text-align: left;">
            <h1>🔍 AI Code Reviewer</h1>
            <h4 style="color: gray;">Get AI-powered code review and suggestions instantly.</h4>
        </div>
        <div style="flex: 1; text-align: right;">
            <img src="https://cdn.prod.website-files.com/6751b9c40053fbf4219732d4/6785268fc609f619d0cddf4a_Generative-AI-for-Code-1-e1695724469521.jpeg" width="400">
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
st.write("---")

# Code Input
st.subheader("📜 Paste Your Code Below:")
code_input = st.text_area("", height=300, placeholder="Write or paste your code here...")

# Review Button with AI Processing
if st.button("🚀 Review Code"):
    if code_input.strip():
        with st.spinner("🔍 Analyzing code... Please wait."):
            review_result = review_code(code_input)
        st.subheader("💡 AI Review & Suggestions:")
        st.write(review_result)
    else:
        st.warning("⚠️ Please enter some code for review.")

# Footer
st.write("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Developed by <b>Yaswanth Kumar Yallapu</b> | Powered by <b>Google Gemini AI</b> | Built with <code>&lt;/&gt;</code> using Streamlit</p>", 
    unsafe_allow_html=True
)
