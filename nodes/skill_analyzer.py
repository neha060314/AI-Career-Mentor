from utils.llm import llm


def skill_analyzer_node(state):

    prompt = f"""
You are a Skill Assessment Expert.

Analyze this student profile.

Name: {state['name']}

Education: {state['education']}

Current Skills: {state['current_skills']}

Target Domain: {state['interested_domain']}

Your task:

1. Identify the student's strong areas.
2. Identify missing technical skills required for the target domain.
3. Give exactly two practical improvement suggestions.

Return the response in clean Markdown.

Format:

### Profile Analysis: <Name>

**Strong Areas**
- ...

**Missing Skills**
- ...

**Improvement Suggestions**
1.
2.

Keep the response concise (under 200 words).
"""

    response = llm.invoke(prompt)

    return {
        "skill_analysis": response.content
    }