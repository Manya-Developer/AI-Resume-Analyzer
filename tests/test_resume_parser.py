from app.tools.resume_parser import extract_resume_text

resume_path = "data/raw/AI_Engineer_Resume.pdf"  # Replace with the actual path to your resume file

text = extract_resume_text(resume_path)

print(text)