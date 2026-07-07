from utils.pdf_reader import extract_text_from_pdf
from utils.llm import llm
import os


def resume_parser_node(state):
    """Parses a resume PDF and extracts Name, Education, and Skills."""

    file_path = input("Enter Resume PDF Path: ").strip()

    # Check if file exists
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return {
            "name": "Candidate",
            "education": "Not Provided",
            "current_skills": "Not Provided",
        }

    # Extract text from PDF
    resume_text = extract_text_from_pdf(file_path)

    prompt = f"""
You are an expert resume parser.

Extract the following information from the resume.

Resume:
{resume_text}

Return ONLY in this exact format:

Name: <Candidate Name>
Education: <Highest Qualification>
Skills: <Comma-separated technical skills>

If any field is missing, write "Not Provided".
"""

    try:
        response = llm.invoke(prompt)
        content = response.content

        # Convert response into plain text
        if isinstance(content, str):
            parsed = content

        elif isinstance(content, list):
            parsed = ""

            for item in content:

                if isinstance(item, str):
                    parsed += item

                elif hasattr(item, "text"):
                    parsed += item.text

                elif isinstance(item, dict):
                    parsed += item.get("text", "")

                else:
                    parsed += str(item)

        else:
            parsed = str(content)

    except Exception as e:
        print(f"❌ Error while calling Gemini: {e}")

        return {
            "name": "Candidate",
            "education": "Not Provided",
            "current_skills": "Not Provided",
        }

    print("\n========== Gemini Response ==========")
    print(parsed)
    print("=====================================\n")

    # Default values
    name = "Candidate"
    education = "Not Provided"
    skills = "Not Provided"

    # Parse response
    for line in parsed.splitlines():

        line = line.strip()

        if line.lower().startswith("name:"):
            name = line.split(":", 1)[1].strip()

        elif line.lower().startswith("education:"):
            education = line.split(":", 1)[1].strip()

        elif line.lower().startswith("skills:"):
            skills = line.split(":", 1)[1].strip()

    return {
        "name": name,
        "education": education,
        "current_skills": skills,
    }