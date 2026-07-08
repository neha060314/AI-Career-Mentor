from graph.builder import career_graph

print("=" * 60)
print("          AI CAREER MENTOR")
print("=" * 60)

print("\nWelcome! This AI system will analyze your profile and")
print("generate a personalized career roadmap.\n")

print("Choose Input Method")
print("-" * 25)
print("1. Upload Resume PDF")
print("2. Manual Profile Entry")

while True:
    choice = input("\nEnter Choice (1/2): ").strip()

    if choice == "1":
        mode = "resume"
        break

    elif choice == "2":
        mode = "manual"
        break

    else:
        print("❌ Invalid choice. Please enter 1 or 2.")

print("\nSuggested Career Domains")
print("-" * 30)
print("• Data Science")
print("• Machine Learning")
print("• AI Engineer")
print("• Data Analyst")
print("• Data Engineer")
print("• Business Analyst")
print("• Full Stack Development")
print("• Backend Development")
print("• Frontend Development")
print("• Cyber Security")
print("• Cloud Computing")

interested_domain = input("\nEnter Target Career Domain: ").strip()

initial_state = {
    "ingestion_mode": mode,
    "interested_domain": interested_domain,
    "name": "",
    "education": "",
    "current_skills": "",
    "skill_analysis": "",
    "roadmap": "",
    "projects": "",
    "interview_prep": ""
}

print("\n" + "=" * 60)
print("Generating Career Report...")
print("=" * 60)

result = career_graph.invoke(initial_state)

print("✔ Resume/Profile Processed")
print("✔ Skill Analysis Completed")
print("✔ Career Roadmap Generated")
print("✔ Portfolio Projects Suggested")
print("✔ Interview Preparation Generated")

report = f"""# AI Career Mentor Report

## Student Profile

- **Name:** {result['name']}
- **Education:** {result['education']}
- **Current Skills:** {result['current_skills']}
- **Target Domain:** {result['interested_domain']}

## Skill Assessment

{result['skill_analysis']}

## Career Roadmap

{result['roadmap']}

## Recommended Projects

{result['projects']}

## Interview Preparation

{result['interview_prep']}

## Final Recommendations

- Dedicate at least 10–12 hours weekly to your learning roadmap.
- Build and publish your projects on GitHub with proper documentation.
- Practice technical interviews consistently and update your resume regularly.
"""

with open("reports/career_report.md", "w", encoding="utf-8") as file:
    file.write(report)

print("\n" + "=" * 60)
print("🎉 Career Report Generated Successfully!")
print("=" * 60)
print("📄 Report Location : reports/career_report.md")
print("=" * 60)