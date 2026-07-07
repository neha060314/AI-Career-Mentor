from typing import TypedDict, Optional


class GraphState(TypedDict):

    ingestion_mode: str

    name: str

    education: str

    current_skills: str

    interested_domain: str

    skill_analysis: Optional[str]

    roadmap: Optional[str]

    projects: Optional[str]

    interview_prep: Optional[str]