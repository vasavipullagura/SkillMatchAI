import streamlit as st

# Page configuration
st.set_page_config(
    page_title="SkillMatch AI",
    page_icon="🎯",
    layout="wide"
)

# Career database
careers = {
    "Python Developer": {
        "skills": ["Python", "SQL", "Git", "Problem Solving"],
        "description": "Build applications and software using Python."
    },
    "Web Developer": {
        "skills": ["HTML", "CSS", "JavaScript", "Git"],
        "description": "Create websites and interactive web applications."
    },
    "Data Analyst": {
        "skills": ["Python", "SQL", "Excel", "Statistics"],
        "description": "Analyze data and discover useful insights."
    },
    "AI Engineer": {
        "skills": ["Python", "Machine Learning", "SQL", "Statistics"],
        "description": "Develop AI systems and machine learning models."
    },
    "Cybersecurity Analyst": {
        "skills": ["Networking", "Linux", "Python", "Problem Solving"],
        "description": "Help protect computers, networks, and information."
    }
}

# Website heading
st.title("🎯 SkillMatch AI")
st.subheader("Discover careers that match your skills")

st.write(
    "Enter your skills to discover suitable career paths "
    "and identify skills you can learn next."
)

# User input
skill_options = sorted({
    skill
    for career in careers.values()
    for skill in career["skills"]
})

selected_skills = st.multiselect(
    "Select the skills you already have:",
    options=skill_options,
    placeholder="Choose one or more skills..."
)

# Additional information
experience = st.selectbox(
    "Your experience level:",
    ["Beginner", "Intermediate", "Advanced"]
)

if st.button("Find My Career Matches", type="primary"):

    if not selected_skills:
        st.warning("Please select at least one skill.")

    else:
        results = []

        # Calculate career match scores
        for career_name, career_info in careers.items():

            required_skills = career_info["skills"]

            matched_skills = [
                skill for skill in required_skills
                if skill in selected_skills
            ]

            missing_skills = [
                skill for skill in required_skills
                if skill not in selected_skills
            ]

            score = round(
                len(matched_skills) / len(required_skills) * 100
            )

            results.append({
                "name": career_name,
                "description": career_info["description"],
                "score": score,
                "matched": matched_skills,
                "missing": missing_skills
            })

        # Show the best matches first
        results.sort(
            key=lambda item: item["score"],
            reverse=True
        )

        st.success("Your career recommendations are ready!")

        st.write(f"**Experience level:** {experience}")

        # Display career recommendations
        for result in results:

            with st.container(border=True):

                st.subheader(result["name"])

                st.write(result["description"])

                st.metric(
                    "Skill Match",
                    f'{result["score"]}%'
                )

                st.progress(result["score"] / 100)

                st.write("✅ **Matching skills**")

                if result["matched"]:
                    st.write(", ".join(result["matched"]))
                else:
                    st.write("No matching skills yet.")

                st.write("📚 **Skills to learn next**")

                if result["missing"]:
                    st.write(", ".join(result["missing"]))
                else:
                    st.write("You have all the listed skills!")

        st.info(
            "These recommendations are based on skill overlap "
            "with a sample career database. They are guidance, "
            "not a guarantee of job eligibility."
        )

# Footer
st.divider()
st.caption("SkillMatch AI | Career Recommendation Demo")