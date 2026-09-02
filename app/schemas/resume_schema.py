## here goes my resume schmea that after extracting the raw code how my output should look like 
# so basically i am gonna structure everything so that it looks good and we can easily pick fields such as skiils education etc etc 


## field is used for defaults such as empty lists
## basemodel allows us to create pydantic models 
## optional allows info to be missing 

from typing import Optional 
from pydantic import BaseModel, Field

class PersonalInfo(BaseModel):
    name : Optional[str] = None
    email : Optional[str] = None
    phone : Optional[str] = None
    address : Optional[str] = None
    linkedin : Optional[str] = None
    github : Optional[str] = None
    portfolio : Optional[str] = None


# PersonalInfo
# ├── name
# ├── email
# ├── phone
# ├── location
# ├── linkedin
# ├── github
# └── portfolio


class Skills(BaseModel):
    programming_languages : list[str] = Field(default_factory = list)
    frameworks: list[str] = Field(default_factory=list)
    libraries: list[str] = Field(default_factory=list)
    tools: list[str] = Field(default_factory=list)
    databases: list[str] = Field(default_factory=list)
    cloud_platforms: list[str] = Field(default_factory=list)
    platforms: list[str] = Field(default_factory=list)
    other: list[str] = Field(default_factory=list)


class Education(BaseModel):
    degree: Optional[str] = None
    institution: Optional[str] = None
    field_of_study: Optional[str] = None
    location: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    grade: Optional[str] = None


class Experience(BaseModel):
    job_title: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None
    employment_type: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    responsibilities: list[str] = Field(default_factory=list)
    technologies: list[str] = Field(default_factory=list)

class Project(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    technologies: list[str] = Field(default_factory=list)
    role: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    url: Optional[str] = None

class Certification(BaseModel):
    name: Optional[str] = None
    issuer: Optional[str] = None
    date: Optional[str] = None
    credential_url: Optional[str] = None

class Training(BaseModel):
    name: Optional[str] = None
    organization: Optional[str] = None
    date: Optional[str] = None
    description: Optional[str] = None

class Publication(BaseModel):
    title: Optional[str] = None
    publisher: Optional[str] = None
    date: Optional[str] = None
    url: Optional[str] = None

class Internship(BaseModel):
    role: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    responsibilities: list[str] = Field(default_factory=list)
    technologies: list[str] = Field(default_factory=list)


class Award(BaseModel):
    name: Optional[str] = None
    issuer: Optional[str] = None
    date: Optional[str] = None
    description: Optional[str] = None


class ResumeProfile(BaseModel):
    personal_info: PersonalInfo = Field(default_factory=PersonalInfo)

    professional_summary: Optional[str] = None

    skills: Skills = Field(default_factory=Skills)

    education: list[Education] = Field(default_factory=list)

    experience: list[Experience] = Field(default_factory=list)

    projects: list[Project] = Field(default_factory=list)

    certifications: list[Certification] = Field(default_factory=list)

    training: list[Training] = Field(default_factory=list)

    achievements: list[str] = Field(default_factory=list)

    publications: list[Publication] = Field(default_factory=list)

    awards: list[Award] = Field(default_factory=list)

    internships: list[Internship] = Field(default_factory=list)

    volunteer_experience: list[str] = Field(default_factory=list)

    languages: list[str] = Field(default_factory=list)

    domains: list[str] = Field(default_factory=list)

    raw_text: Optional[str] = None