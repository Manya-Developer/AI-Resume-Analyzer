from app.tools.resume_parser import extract_resume_text

resume_path = "data/raw/Updated_generalised_cv.docx"

text = extract_resume_text(resume_path)

print(text)