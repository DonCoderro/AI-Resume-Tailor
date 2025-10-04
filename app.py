import streamlit as st
import tempfile
from parsers import analyze_cv_against_offer, get_text_from_cv, get_text_from_job_offer
from utils import safe_run


st.title("AI Resume Tailor")

cv_file = st.file_uploader("Upload your CV", type=["docx", "pdf"])
offer_file = st.file_uploader("Upload job offer", type=["htm"])


if st.button("Analyze"):

    if cv_file and offer_file:
        with st.spinner("Analyzing documents..."):
            with tempfile.NamedTemporaryFile(delete=False, suffix=cv_file.name) as tmp:
                tmp.write(cv_file.read())
                tmp_cv_path = tmp.name

            with tempfile.NamedTemporaryFile(delete=False, suffix=offer_file.name) as tmp:
                tmp.write(offer_file.read())
                tmp_offer_path = tmp.name

            cv_text = safe_run(get_text_from_cv, tmp_cv_path)
            offer_text = safe_run(get_text_from_job_offer, tmp_offer_path)

            result = analyze_cv_against_offer(cv_text, offer_text)

            st.session_state.result = result

if "result" in st.session_state:
    st.text_area(
        label="Result",
        value=st.session_state.result,
        height=400)

    st.download_button(
        label="Download result",
        data=st.session_state.result,
        file_name="result.txt",
        mime="text/plain"
    )

# streamlit run app.py --server.headless=true --server.runOnSave=true
