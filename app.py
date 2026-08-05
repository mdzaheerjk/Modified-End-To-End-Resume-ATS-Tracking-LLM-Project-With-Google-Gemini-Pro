import streamlit as st
from google import genai


st.set_page_config(
    page_title="Smart ATS Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


st.sidebar.title("⚙️ Settings")

api_key = st.sidebar.text_input(
    "Enter Google Gemini API Key",
    type="password",
    placeholder="AIzaSy..."
)

st.sidebar.markdown("---")
st.sidebar.markdown(
"""
### How to Use

1. Enter your Gemini API Key.
2. Paste the Job Description.
3. Upload your Resume (PDF).
4. Click **Analyze Resume**.
"""
)


st.title("📄 Smart ATS Resume Analyzer")
st.caption("Analyze your resume against any Job Description using Gemini AI.")

job_description = st.text_area(
    "Job Description",
    height=220,
    placeholder="Paste the complete Job Description..."
)

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

analyze = st.button(
    "🚀 Analyze Resume",
    use_container_width=True
)


PROMPT = """
You are a highly experienced Applicant Tracking System (ATS) and Technical Recruiter.

Analyze the uploaded resume against the provided Job Description.

Return your response in Markdown using the following format:

# ATS Match
- Match Percentage

# Missing Keywords
- keyword 1
- keyword 2

# Matching Skills
- skill 1
- skill 2

# Strengths

# Weaknesses

# Suggestions for Improvement

# Final Verdict
"""

def analyze_resume(client, pdf_file, jd):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=[
            PROMPT,
            jd,
            pdf_file
        ]
    )

    return response.text

if analyze:

    if not api_key:
        st.error("Please enter your Gemini API Key.")
        st.stop()

    if uploaded_file is None:
        st.error("Please upload your resume.")
        st.stop()

    if not job_description.strip():
        st.error("Please enter the Job Description.")
        st.stop()

    try:

        client = genai.Client(api_key=api_key)

        with st.spinner("Uploading Resume..."):

            pdf_file = client.files.upload(
                file=uploaded_file,
                config={
                    "mime_type": "application/pdf"
                }
            )

        with st.spinner("Analyzing Resume..."):

            result = analyze_resume(
                client,
                pdf_file,
                job_description
            )

        st.success("Analysis Completed Successfully!")

        st.markdown(result)

    except Exception as e:
        st.error(f"Error: {e}")
