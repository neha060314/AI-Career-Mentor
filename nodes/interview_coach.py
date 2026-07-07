from utils.llm import llm


def interview_coach_node(state):

    prompt = f"""
You are a Technical Interview Coach.

Student

{state['name']}

Target Domain

{state['interested_domain']}

Roadmap

{state['roadmap']}

Generate

## Technical Questions

2 questions

## HR Questions

2 questions

## Mistakes to Avoid

2 interview mistakes

Return clean Markdown.

Keep the response under 200 words.
"""

    response = llm.invoke(prompt)

    return {
        "interview_prep": response.content
    }