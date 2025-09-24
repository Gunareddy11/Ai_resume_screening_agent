🤖 AI Resume Screening Agent — Project Report
1. Title

AI-Powered Resume Screening Agent using LLMs + RAG (Retrieval-Augmented Generation)

2. Abstract

Recruitment teams spend a large portion of their time filtering resumes, often manually scanning hundreds of applications. This project builds an AI Resume Screening Agent that automates candidate shortlisting. It uses Natural Language Processing (NLP), Large Language Models (LLMs), and RAG (Retrieval-Augmented Generation) to evaluate resumes against job descriptions, rank candidates, and provide interpretable feedback for hiring managers.

3. Objectives

Parse resumes (PDF/DOCX/Plain Text) into structured candidate profiles.

Match resumes with specific job descriptions (JDs).

Provide a fit score and ranking of candidates.

Highlight strengths, weaknesses, and missing skills.

Ensure fair, unbiased recommendations using explainable AI.

4. System Architecture

Step-by-step workflow:

Data Ingestion

Input: Resumes (PDF/DOCX) + Job Description text.

Parsing: PyPDF2, docx2txt, or Textract.

Preprocessing & Feature Extraction

Convert resumes into structured text (Name, Skills, Experience, Education).

Extract job requirements (skills, experience, tools, certifications).

Embedding & Vectorization

Use embeddings (sentence-transformers or OpenAI embeddings) to convert resumes & JDs into vector space.

RAG Pipeline

Store embeddings in Vector Database (FAISS / ChromaDB).

Retrieve top candidate chunks relevant to job description queries.

LLM Screening Agent

Use an LLM (e.g., Llama 2, GPT, or open-source model) with a prompt template:
“Given a job description and a candidate resume, rate candidate fit (0–100), list matching skills, missing skills, and provide a short recommendation.”

Output & Ranking

Fit Score (0–100).

Candidate ranking (sorted).

Recommendation summary for recruiter.

Deployment

Streamlit / FastAPI UI for recruiters.

Upload resumes + JD → Get ranked results + explanations.

5. Tools & Technologies

NLP / LLMs: HuggingFace Transformers, OpenAI GPT (optional), LLaMA-2, Flan-T5.

Embeddings: Sentence-BERT (all-MiniLM-L6-v2).

Vector Database: FAISS / Chroma.

Backend: Python (FastAPI, LangChain).

Frontend: Streamlit Dashboard.

Parsing Libraries: PyPDF2, python-docx, Textract.

6. Model Design
6.1 Resume Parsing

Extract structured fields (Name, Email, Skills, Experience, Education).

Use regex + Named Entity Recognition (NER) for accuracy.

6.2 Semantic Similarity

Compute cosine similarity between candidate embeddings & JD embeddings.

Weighted scoring:

Skills (50%)

Experience (30%)

Education (20%)

6.3 Screening with LLM + RAG

Retrieve top skills/experience from vector DB.

LLM generates:

Candidate fit score.

Matching skills.

Missing skills.

Recommendation text.

7. Evaluation
7.1 Metrics

Accuracy of Skill Extraction (NER F1-score).

Ranking Quality (Kendall’s Tau / Spearman correlation vs HR ranking).

LLM Output Evaluation: BLEU / ROUGE for summaries, human recruiter validation.
