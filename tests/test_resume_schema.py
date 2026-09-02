from app.schemas.resume_schema import ResumeProfile


resume = ResumeProfile(
    personal_info={
        "name": "Manya Verma",
        "email": "manyaverma135@gmail.com"
    },
    skills={
        "programming_languages": ["Python", "Java", "C++"],
        "libraries": ["NumPy", "Pandas", "Scikit-learn"],
        "tools": ["Git", "Docker"]
    },
    domains=[
        "Artificial Intelligence",
        "Machine Learning",
        "Computer Vision"
    ]
)

print(resume)