# resume_processor.py

import docx
import json
import re

# Parse resume text from uploaded .docx file
def parse_resume(docx_file):
    doc = docx.Document(docx_file)
    full_text = [para.text for para in doc.paragraphs]
    return "\n".join(full_text)

# Clean resume text: lowercase and remove special characters
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

# Match keywords from the bank with the resume
# Match keywords from the bank with the resume
def match_keywords(resume_text, role):
    with open("utils/keyword_bank.json") as f:
        keywords = json.load(f)

    # Ensure role is a string
    if isinstance(role, list):
        role = role[0]  # Or handle as needed
    elif not isinstance(role, str):
        role = str(role)

    required_keywords = keywords.get(role, [])
    
    cleaned_resume = clean_text(resume_text)
    matched = [kw for kw in required_keywords if kw.lower() in cleaned_resume]
    return matched




# Calculate matching percentage
def calculate_fit_score(matched_keywords, total_keywords_count):
    if total_keywords_count == 0:
        return 0
    return round((len(matched_keywords) / total_keywords_count) * 100, 2)


