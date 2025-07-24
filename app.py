import streamlit as st
from resume_processor import parse_resume, match_keywords, calculate_fit_score
import json

st.title("🧠 AI Resume Screening Agent")

uploaded_file = st.file_uploader("📄 Upload a resume (DOCX)", type="docx")
role = st.selectbox("🎯 Select Job Role", ["Data Scientist", "Frontend Developer", "Backend Developer"])

if uploaded_file and role:
    parsed_info = parse_resume(uploaded_file)
    st.subheader("🔍 Extracted Resume Text")
    st.write(parsed_info)

    with open("utils/keyword_bank.json") as f:
        keyword_bank = json.load(f)
    
    required_keywords = keyword_bank.get(role, [])
    matched_keywords = match_keywords(parsed_info, required_keywords)
    score = calculate_fit_score(matched_keywords, len(required_keywords))

    st.subheader("✅ Matched Skills")
    st.write(matched_keywords)
    st.metric("📊 Fit Score", f"{score}%")
