import streamlit as st

# -------------------------------
# Portfolio Configuration
# -------------------------------
st.set_page_config(page_title="Leonard Phokane Portfolio", layout="wide")

# Custom CSS for glowing cards and dark theme
st.markdown("""
    <style>
    body {
        background-color: #0e1117;
        color: #fafafa;
    }
    .card {
        background: #1c1f26;
        border-radius: 12px;
        padding: 20px;
        margin: 10px;
        box-shadow: 0 0 15px rgba(0,255,255,0.3);
    }
    .banner {
        width: 100%;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    footer {
        text-align: center;
        padding: 20px;
        font-size: 14px;
        color: #888;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# Sidebar Navigation
# -------------------------------
st.sidebar.title("Navigation")
section = st.sidebar.radio(
    "Go to",
    ["Profile", "Skills", "Experience", "Education", "Projects", "Contact"]
)

# -------------------------------
# Profile Section
# -------------------------------
if section == "Profile":
    st.title("Leonard Phokane")
    st.subheader("AI/ML Engineer | Freelance Full‑Stack & Backend Engineer | Cloud‑Native & DevOps Engineer Intern")
    st.caption("Building scalable pipelines, modernizing applications, and deploying intelligent systems in hybrid cloud environments.")

    st.image("attachments/profile.png", width=250)  # Profile picture

    st.markdown("""
    I am a Cloud‑Native & DevOps Engineer, advancing expertise through IBM’s Cloud‑Native Learning Journey while serving as a Backend AI Engineering Intern at FlyRank AI.  
    With 10+ years in full‑stack development, cloud infrastructure, and AI integration, I specialize in scalable pipelines, OpenShift deployments, and intelligent systems.
    """)

# -------------------------------
# Skills Section
# -------------------------------
elif section == "Skills":
    st.header("Skills with Metrics")

    skills = {
        "Python": 90,
        "Node.js": 85,
        "React": 80,
        "PostgreSQL": 80,
        "CI/CD Automation": 95,
        "Cloud‑Native (OpenShift, Kubernetes, Docker)": 90,
        "AI/ML Model Optimization": 85
    }

    for skill, value in skills.items():
        st.write(f"{skill} ({value}%)")
        st.progress(value)

# -------------------------------
# Experience Section
# -------------------------------
elif section == "Experience":
    st.header("Experience")
    st.markdown("""
    - **Cloud‑Native & DevOps Intern** – IBM Tech Training  
    - **Machine Learning Engineering Intern** (Completed, 2026)  
    - **Backend AI Engineering Intern** (Current) – FlyRank AI  
    - **Freelance Full‑Stack Developer & AI Engineer** – Independent Projects (2017–Present)  
    """)

# -------------------------------
# Education Section
# -------------------------------
elif section == "Education":
    st.header("Education")
    st.markdown("""
    - **Power Learn Project** – Software Development (2025)  
    - **University of Johannesburg / FNB App Academy** – Future Digital Skills Programme (2026)  
    - **University of South Africa** – BSc Computer Science (2012)  
    """)

# -------------------------------
# Projects Section
# -------------------------------
elif section == "Projects":
    st.header("Featured Projects")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image("attachments/cloud-devops.png", use_container_width=True)
        st.markdown("**Cloud & DevOps Internship Project**")
        st.caption("Containerised Node.js app with CI/CD automation and monitoring.")
        st.link_button("View Project", "https://github.com/leonardphokane/cloud-devops-demo")

    with col2:
        st.image("attachments/machine-learning.png", use_container_width=True)
        st.markdown("**Machine Learning Internship Project**")
        st.caption("AI pipelines and enterprise solutions at FlyRank AI.")
        st.link_button("View Project", "https://github.com/leonardphokane/machine-learning-internship")

    with col3:
        st.image("attachments/fullstack.png", use_container_width=True)
        st.markdown("**Fullstack Internship App**")
        st.caption("End‑to‑end web platform with React, Node.js, and PostgreSQL.")
        st.link_button("View Project", "https://github.com/leonardphokane/fullstack-internship-app")

    with col4:
        st.image("attachments/payment-transfer-api.png", use_container_width=True)
        st.markdown("**Payment Service API (Independent Project, Ongoing)**")
        st.caption("""
        ○ Secure, idempotent REST endpoint in Java (Spring Boot)  
        ○ Focused on financial transaction reliability and API robustness
        """)
        st.link_button("View Project", "https://github.com/leonardphokane/payment-service/tree/main")

# -------------------------------
# Contact Section
# -------------------------------
elif section == "Contact":
    st.header("Contact")
    st.markdown("""
    📧 **Email:** leonardphokane1@gmail.com  
    🔗 **LinkedIn:** [linkedin.com/in/leonardphokane](https://linkedin.com/in/leonardphokane)  
    💻 **GitHub:** [github.com/leonardphokane](https://github.com/leonardphokane)  
    📍 **Location:** Johannesburg, South Africa  
    """)

# -------------------------------
# Footer
# -------------------------------
st.markdown("<footer>© 2026 Leonard Phokane | Built with Streamlit</footer>", unsafe_allow_html=True)
