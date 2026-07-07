from utils.llm import llm


def roadmap_generator_node(state):

    prompt = f"""
You are a Career Roadmap Specialist.

Student Profile

{state['skill_analysis']}

Target Domain:
{state['interested_domain']}

Create a structured 3-month learning roadmap.

Include

Month 1

Month 2

Month 3

For every month include

• Focus
• Actions
• Goal

Finally recommend

• Technologies
• Certifications

Return in Markdown.

Keep it under 250 words.
"""

    response = llm.invoke(prompt)

    return {
        "roadmap": response.content
    }