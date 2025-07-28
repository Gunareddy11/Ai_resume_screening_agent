import streamlit as st
from resume_processor import parse_resume, match_keywords, calculate_fit_score
import json
import os  # <-- added

st.title("🧠 AI Resume Screening Agent")

uploaded_file = st.file_uploader("📄 Upload a resume (DOCX)", type="docx")
role = st.selectbox("🎯 Select Job Role", ["Data Scientist", "Frontend Developer", "Backend Developer", "Data Analyst"])

if uploaded_file and role:
    parsed_info = parse_resume(uploaded_file)
    st.subheader("🔍 Extracted Resume Text")
    st.write(parsed_info)

    # ✅ Robust path handling
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(BASE_DIR, "utils", "keyword_bank.json")

    with open(json_path) as f:
        keyword_bank = json.load(f)

    required_keywords = keyword_bank.get(role, [])
    matched_keywords = match_keywords(parsed_info, required_keywords)
    score = calculate_fit_score(matched_keywords, len(required_keywords))

    st.subheader("✅ Matched Skills")
    st.write(matched_keywords)

    st.subheader("📊 Fit Score")
    st.write(f"{score}% match for {role}")
