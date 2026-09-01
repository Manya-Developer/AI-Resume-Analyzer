from pathlib import Path

import pymupdf  # PyMuPDF
from docx import Document


def extract_text_from_pdf(file_path: str) -> str:
    """
    Extract text from a PDF resume.

    Args:
        file_path: Path to the PDF file.

    Returns:
        Extracted text from all pages.
    """

    document = pymupdf.open(file_path)

    pages_text = []

    for page in document:
        text = page.get_text()
        pages_text.append(text)

    document.close()

    return "\n".join(pages_text).strip()


def extract_text_from_docx(file_path: str) -> str:
    """
    Extract text from a DOCX resume.

    Args:
        file_path: Path to the DOCX file.

    Returns:
        Extracted text from the document.
    """

    document = Document(file_path)

    paragraphs = []

    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            paragraphs.append(paragraph.text.strip())

    return "\n".join(paragraphs)


def extract_resume_text(file_path: str) -> str:
    """
    Extract text from a PDF or DOCX resume.

    Args:
        file_path: Path to the resume file.

    Returns:
        Extracted resume text.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file format is unsupported.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Resume file not found: {file_path}"
        )

    extension = path.suffix.lower()

    if extension == ".pdf":
        return extract_text_from_pdf(file_path)

    elif extension == ".docx":
        return extract_text_from_docx(file_path)

    else:
        raise ValueError(
            "Unsupported file format. "
            "Only PDF and DOCX files are supported."
        )