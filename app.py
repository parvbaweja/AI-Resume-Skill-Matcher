import gradio as gr

TARGET_SKILLS = {
    'python', 'java', 'c++', 'javascript', 'node.js', 'express', 'react',
    'next.js', 'angular', 'html', 'css', 'sql', 'mysql', 'mongodb', 'supabase',
    'aws', 'git', 'rest', 'api', 'docker', 'kubernetes', 'flask', 'fastapi'
}

def extract_skills(text):
    text = text.lower()
    return {skill for skill in TARGET_SKILLS if skill in text}

def match_skills(resume_text, jd_text):
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)
    matched = resume_skills & jd_skills
    missing = jd_skills - resume_skills
    match_percent = round(len(matched) / len(jd_skills) * 100, 2) if jd_skills else 0

    result = f"✅ Skill Match Score: {match_percent}%\\n\\n"
    result += "🟩 Matched Skills:\\n" + ", ".join(sorted(matched)) + "\\n\\n"
    result += "❌ Missing Skills:\\n" + ", ".join(sorted(missing))
    return result

demo = gr.Interface(
    fn=match_skills,
    inputs=[
        gr.Textbox(lines=15, label="Paste Resume Text"),
        gr.Textbox(lines=15, label="Paste Job Description Text")
    ],
    outputs="text",
    title="🧠 AI Resume Skill Matcher",
    description="Paste your resume and job description to compare skills and get a match percentage!"
)

demo.launch()
