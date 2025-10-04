# AI Resume Tailor

An application that tailors your CV to a specific job offer using AI (OpenAI GPT).
It allows you to upload a CV file (.pdf, .docx) and a job offer (.htm), then generates suggestions on how to improve your CV to increase your chances of getting hired.

---

## 🚀 Features
- Parsing CVs from PDF and DOCX files.
- Extracting job descriptions from HTML files.
- Analyzing the CV against the job description using an OpenAI model.
- Web application built with **Streamlit**.
- Error logging to `errors.log`.

---

## 📂 Project Strucutre
 AI Resume Tailor/
├── app.py # Main Streamlit app
├── parsers.py # File parsing logic & OpenAI integration
├── utils.py # Utility functions & error handling
├── errors.log # Error log file
├── requirements.txt # List of dependencies
└── README.md
---

## ⚙️ Installation

1. Clone the repository:

   git clone https://github.com/DonCoderro/AI-Resume-Tailor.git
   cd ai-resume-tailor

2. Create a virtual environment and install dependencies:

    python -m venv venv
    source venv/bin/activate   # Linux/macOS
    venv\Scripts\activate      # Windows
    pip install -r requirements.txt

3. Configure the .env file:

    OPEN_AI_API_TOKEN=your_OPENAI_token

## Running the app

    streamlit run app.py

## 📝 Example usage

    In the Streamlit app, upload your CV (.pdf or .docx).

    Upload a job offer file (.htm).

    Click Analyze – the app will generate suggestions on how to improve your CV.
