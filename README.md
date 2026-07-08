# AI Career Mentor

An intelligent multi-agent career guidance system powered by LangGraph and Google Gemini that analyzes student profiles, identifies skill gaps, generates personalized career roadmaps, recommends portfolio projects, and prepares users for technical interviews.

![Python](https://img.shields.io/badge/Python-3.13+-blue?style=for-the-badge&logo=python)
![LangGraph](https://img.shields.io/badge/LangGraph-Multi--Agent-success?style=for-the-badge)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-orange?style=for-the-badge&logo=google)

---

# Overview

Choosing the right career path requires understanding current skills, identifying gaps, and planning a structured learning journey.

**AI Career Mentor** is an Agentic AI application built using **LangGraph** that orchestrates a team of specialized AI agents collaborating to provide personalized career guidance.

Instead of relying on a single prompt, the system follows a structured workflow where each AI agent performs a dedicated responsibility before passing the information to the next agent.

The application supports two modes of profile ingestion:

- 📄 Resume PDF Upload
- ⌨️ Manual Profile Entry

Based on the student's profile and target career domain, the system automatically generates:

- Skill Gap Analysis
- Personalized Career Roadmap
- Portfolio Project Recommendations
- Interview Preparation Guide
- Comprehensive Career Report

---

# Features

- Resume PDF Parsing
- Manual Student Profile Entry
- Multi-Agent Workflow using LangGraph
- Google Gemini Integration
- Skill Gap Analysis
- Personalized 3-Month Learning Roadmap
- Beginner, Intermediate & Advanced Project Recommendations
- Technical & HR Interview Preparation
- Automatic Career Report Generation
- Modular Python Project Structure

---

# System Architecture

```
                    START
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
 Resume PDF Upload         Manual Input
          │                       │
          └───────────┬───────────┘
                      │
                      ▼
          Skill Assessment Agent
                      │
                      ▼
         Career Roadmap Agent
                      │
                      ▼
        Portfolio Mentor Agent
                      │
                      ▼
       Technical Interview Coach
                      │
                      ▼
             Career Report Generator
                      │
                      ▼
                     END
```

---

# 🤖 AI Agents

## Resume Parser Agent

Responsible for extracting student information from a PDF resume.

Extracts:

- Name
- Education
- Technical Skills

---

## Skill Assessment Agent

Analyzes the student's current profile against the selected career domain.

Produces:

- Strong Areas
- Missing Skills
- Improvement Suggestions

---

## Career Roadmap Agent

Creates a personalized learning roadmap.

Includes:

- Month 1 Goals
- Month 2 Goals
- Month 3 Goals
- Technology Recommendations
- Certification Suggestions

---

## Portfolio Mentor Agent

Suggests three portfolio projects.

- Beginner Project
- Intermediate Project
- Advanced Project

Each project includes:

- Description
- Skills Learned

---

## Interview Coach Agent

Prepares students for placements.

Generates:

- Technical Questions
- HR Questions
- Interview Preparation Tips

---

# 📂 Project Structure

```
AI-Career-Mentor/
│
├── graph/
│   ├── __init__.py
│   ├── builder.py
│   ├── router.py
│   └── state.py
│
├── nodes/
│   ├── __init__.py
│   ├── resume_parser.py
│   ├── manual_input.py
│   ├── skill_analyzer.py
│   ├── roadmap_generator.py
│   ├── project_mentor.py
│   └── interview_coach.py
│
├── reports/
│   ├── career_report.md (automatically generated after running)
│
├── resumes/
│   ├── sample_resume.pdf (you can add any resume)
│
├── utils/
│   ├── __init__.py
│   ├── llm.py
│   └── pdf_reader.py
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── main.py
```

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| LangGraph | Multi-Agent Workflow |
| LangChain | LLM Framework |
| Google Gemini | Large Language Model |
| PyPDF | Resume Parsing |
| python-dotenv | Environment Variables |

---

# Installation

## Clone Repository

```bash
git clone https://github.com/neha060314/AI-Career-Mentor.git

cd AI-Career-Mentor
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Configure API Key

Create a `.env` file in the project root directory.

```env
GEMINI_API_KEY=your_api_key_here
```

---

# Running the Project

```bash
python main.py
```

---


# Sample Report

The generated report contains:

- Student Profile
- Skill Assessment
- Career Roadmap
- Recommended Portfolio Projects
- Interview Preparation
- Final Recommendations

The report is automatically saved as:

```
reports/career_report.md
```

---


# Screenshots

## Application

![Terminal](screenshots\terminal.png)

## Generated Report

![Report](screenshots\report.png)

---

## If you found this project useful, consider giving it a Star!

It helps others discover the project and motivates future improvements.