from langgraph.graph import StateGraph, START, END

from graph.state import GraphState
from graph.router import routing_condition

from nodes.resume_parser import resume_parser_node
from nodes.manual_input import manual_input_node
from nodes.skill_analyzer import skill_analyzer_node
from nodes.roadmap_generator import roadmap_generator_node
from nodes.project_mentor import project_mentor_node
from nodes.interview_coach import interview_coach_node


builder = StateGraph(GraphState)

builder.add_node("resume_parser", resume_parser_node)

builder.add_node("manual_input", manual_input_node)

builder.add_node("skill_analyzer", skill_analyzer_node)

builder.add_node("roadmap_generator", roadmap_generator_node)

builder.add_node("project_mentor", project_mentor_node)

builder.add_node("interview_coach", interview_coach_node)

builder.add_conditional_edges(

    START,

    routing_condition,

    {

        "resume_parser": "resume_parser",

        "manual_input": "manual_input"

    }

)

builder.add_edge("resume_parser", "skill_analyzer")

builder.add_edge("manual_input", "skill_analyzer")

builder.add_edge("skill_analyzer", "roadmap_generator")

builder.add_edge("roadmap_generator", "project_mentor")

builder.add_edge("project_mentor", "interview_coach")

builder.add_edge("interview_coach", END)

career_graph = builder.compile()