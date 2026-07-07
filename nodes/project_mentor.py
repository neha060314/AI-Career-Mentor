from utils.llm import llm


def project_mentor_node(state):

    prompt = f"""
You are an AI Project Mentor.

Target Domain

{state['interested_domain']}

Roadmap

{state['roadmap']}

Suggest exactly three portfolio projects.

1. Beginner

2. Intermediate

3. Advanced

For each project include

Project Name

Description

Skills Learned

Return clean Markdown.

Keep the response under 250 words.
"""

    response = llm.invoke(prompt)

    return {
        "projects": response.content
    }