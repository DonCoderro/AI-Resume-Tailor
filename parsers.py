import os
from bs4 import BeautifulSoup
from utils import clean_job_offer_text
from dotenv import load_dotenv
import os
from openai import OpenAI
import docx
from PyPDF2 import PdfReader

PROMPT_TEXT = "Jesteś ekspertem w dziale rekrutacji. Masz przed sobą opis stanowiska, na które poszukujecie kandydata oraz CV kandydata. Co powinien zmienić kandydat aby jego CV lepiej pasowało do oferty."

load_dotenv()
token = os.getenv("OPEN_AI_API_TOKEN")


def get_text_from_cv(cv_file_path: str) -> str:

    ext = os.path.splitext(cv_file_path)[-1].lower()

    if ext == ".pdf":
        cv_file = PdfReader(cv_file_path)
        full_text = [page.extract_text() for page in cv_file.pages]
        return "\n".join(full_text)

    elif ext == ".docx":
        doc = docx.Document(cv_file_path)
        full_text = [para.text for para in doc.paragraphs]
        return '\n'.join(full_text)


def get_text_from_job_offer(job_offer_file_path: str) -> str:
    with open(job_offer_file_path, "r", encoding="utf-8") as file:
        html = file.read()

    soup = BeautifulSoup(html, "html.parser")
    all_text = soup.get_text(separator="\n", strip=True)

    all_text = clean_job_offer_text(all_text)

    return all_text


def build_prompt(cv_text: str, offer_text: str) -> str:
    return f"""{PROMPT_TEXT}

    CV TEXT:
    {cv_text}

    JOB OFFER TEXT:
    {offer_text}
    """


def analyze_cv_against_offer(cv_text: str, offer_text: str) -> str:

    prompt = build_prompt(cv_text, offer_text)

    client = OpenAI(api_key=token)

    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role": "system",
                "content": "Jesteś ekspertem HR, poprawiasz CV, nie zadajesz pytań, odpowiadasz w języku, w którym napisane jest CV"},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
