
# Smart ATS Resume Analyzer — Enhanced with Google Gemini

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)  
A lightweight Streamlit app that analyzes your resume (PDF) against any Job Description using Google Gemini (google-genai). It simulates an Applicant Tracking System (ATS) + recruiter analysis and returns a structured Markdown report: match percentage, missing keywords, matching skills, strengths, weaknesses, and improvement suggestions.

Why this repo exists
- Quickly get ATS-style feedback without setting up heavyweight tooling.
- Use Gemini’s generative capabilities to surface keyword gaps, skill matches, and plain-language suggestions.
- Great for job seekers, resume coaches, or small recruiting teams.

Highlights
- Single-file Streamlit app (app.py) — easy to run and customize.
- Uses google-genai for uploading files and generating content via Gemini models.
- Output returned in Markdown for easy copy/paste or display.

Demo screenshot
- Open the app locally and paste a job description, upload a PDF resume, enter your Gemini API key, and click "Analyze Resume" to see the output.

Contents
- app.py — Streamlit application and prompt used for analysis
- requirements.txt — Python dependencies (streamlit, google-genai)
- LICENSE — MIT (you may reuse and modify)

Requirements
- Python 3.10+ recommended
- A Google Gemini API key (google-genai) with file upload and model access
- pip

Setup (local)
1. Clone the repo
   git clone https://github.com/mdzaheerjk/Modified-End-To-End-Resume-ATS-Tracking-LLM-Project-With-Google-Gemini-Pro.git
   cd Modified-End-To-End-Resume-ATS-Tracking-LLM-Project-With-Google-Gemini-Pro

2. Create and activate a virtual environment (optional but recommended)
   python -m venv .venv
   source .venv/bin/activate  # macOS / Linux
   .venv\Scripts\activate     # Windows (PowerShell)

3. Install dependencies
   pip install -r requirements.txt

Run
- Start the Streamlit app:
  streamlit run app.py

- In the Streamlit UI:
  1. Enter your Gemini API Key in the left sidebar (it's asked as a masked text field).
  2. Paste the Job Description into the Job Description box.
  3. Upload your resume as a PDF.
  4. Click "🚀 Analyze Resume".

Notes about the Gemini integration
- app.py uses google.genai.Client(api_key=...) and:
  - client.files.upload(file=uploaded_file, config={"mime_type": "application/pdf"})
  - client.models.generate_content(model="gemini-3.6-flash", contents=[PROMPT, job_description, pdf_file])
- The app sends the job description, a fixed PROMPT (which instructs Gemini to output structured Markdown), and the uploaded PDF file reference to the model.

Security & privacy
- Your Gemini API key is entered in the UI. Never commit your key to source control.
- Uploaded resumes are uploaded to the Google Gemini service via the client; treat uploads as potentially persistent. If you require local-only processing, replace the upload & model call with a local resume parser + different model/service or a privacy-focused flow.
- Consider redaction if you plan to use sensitive or PII-heavy resumes.

Customization ideas
- Replace or enrich the PROMPT in app.py to tailor the report (e.g., prioritize senior-level experience, target specific skills, or format for ATS scoring).
- Preprocess the PDF to extract sections (name, contact, experience, education) and send structured inputs to Gemini for more precise matching.
- Add support for DOCX, TXT, or direct LinkedIn profile URL parsing.
- Add logging, tests, and a CI pipeline (GitHub Actions) to validate dependencies and runs.

Example prompt / expected output format
The PROMPT included in app.py asks Gemini to return a Markdown report with sections:
- # ATS Match (Match Percentage)
- # Missing Keywords (list)
- # Matching Skills (list)
- # Strengths
- # Weaknesses
- # Suggestions for Improvement
- # Final Verdict

Troubleshooting
- If the app fails to upload or analyze:
  - Check your Gemini API key and model access.
  - Confirm the google-genai package version matches the REST API/SDK expectations (see requirements.txt).
  - Confirm the uploaded file is a valid PDF.

Development & testing notes
- app.py is intentionally simple so you can easily extend it. To add tests:
  - Factor Gemini interactions into a helper module and mock google-genai client methods.
  - Add unit tests to assert prompt generation, input validation, and local parsing behavior.

Contributing
- Contributions are welcome. Open issues for feature requests, bugs, or improvements.
- For code contributions: fork the repo, create a feature branch, and open a pull request with a clear description.

License
- MIT License — see LICENSE.

Acknowledgements
- Built using Streamlit and Google Gemini (google-genai).
- Inspired by common ATS practices and resume coaching workflows.

Contact
- Author: Mohd Zaheeruddin (from LICENSE)
- For feedback or help, open an issue on this repository.

Quick changelog
- 2026 — Initial Streamlit + Google Gemini integration

````

What I did and what's next
- I inspected the repo's top-level files (app.py, requirements.txt, LICENSE, .vscode) and read app.py to confirm behavior and exact prompt structure.
- I drafted the README above tailored to the code and usage patterns found.
- If you'd like, I can:
  - Commit this README.md to the repo for you.
  - Improve the prompt in app.py (more detailed scoring rubric).
  - Add a small PDF-to-text preprocessor for better results and local previews.
Which would you like me to do next?
