import streamlit as st

# ---- Page Config ----
st.set_page_config(page_title="Syeda Gulzar Bano | Portfolio", layout="wide")

# ---- Custom CSS ----
st.markdown("""
<style>
    body {
        font-family: 'Arial', sans-serif;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 24px;
        border-radius: 8px;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .project-card {
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 16px;
        margin: 16px 0;
        background-color: white;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .project-card img {
        width: 100%;
        border-radius: 8px;
    }
    .project-card a {
        color: #4CAF50;
        text-decoration: none;
    }
    .project-card a:hover {
        text-decoration: underline;
    }
</style>
""", unsafe_allow_html=True)

# ---- Sidebar Navigation ----
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Home", "About", "Projects", "Contact", "Socials"))

# ---- Home ----
if page == "Home":
    st.title("Welcome to Syeda Gulzar Bano's Portfolio 🚀")
    st.subheader("Fullstack Developer | Web & App Enthusiast")
    st.write("Explore my portfolio to learn more about my skills, projects, and achievements.")

    st.markdown("### Let's build something incredible together!")

    if st.button("View My Projects"):
        st.experimental_set_query_params(page="Projects")

# ---- About ----
elif page == "About":
    st.title("About Me")
    st.write("I'm a **Fullstack Developer** with expertise in building modern web applications.")

    st.markdown("### 🎓 Education")
    st.write("- Graduate (Currently pursuing higher education)")

    st.markdown("### 💻 Skills")
    st.write("- Frontend: HTML, CSS, JavaScript, React")
    st.write("- Backend: Node.js, Python, Django")
    st.write("- Databases: MongoDB, MySQL")
    st.write("- Tools: Git, Docker, Streamlit")

    st.markdown("### 📄 Download My Resume")
    with open("sample_resume.txt", "w") as f:
        f.write("Syeda Gulzar Bano - Fullstack Developer\n\nSkills: Python, JavaScript, React, Node.js, MongoDB")
    with open("sample_resume.txt", "rb") as f:
        st.download_button("Download Resume", data=f, file_name="Syeda_Resume.txt")

# ---- Projects ----
elif page == "Projects":
    st.title("My Projects")
    st.subheader("Portfolio Projects")

    portfolio_projects = [
        {
            "title": "Portfolio Website",
            "description": "A fully responsive portfolio website built with React and deployed on Vercel.",
            "image": "https://via.placeholder.com/300x200?text=Portfolio+Website",
            "link": "https://portfolio.vercel.app/"
        },
        {
            "title": "E-Commerce Website",
            "description": "An e-commerce platform built with React and Node.js.",
            "image": "https://via.placeholder.com/300x200?text=E-Commerce+Website",
            "link": "https://E-Commerce.vercel.app/"
        }
    ]

    for proj in portfolio_projects:
        st.markdown(f"""
        <div class="project-card">
            <h3>{proj['title']}</h3>
            <img src="{proj['image']}" alt="{proj['title']} Screenshot">
            <p>{proj['description']}</p>
            <a href="{proj['link']}" target="_blank">View Project</a>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("Streamlit Projects")

    streamlit_projects = [
        {
            "title": "BMI Calculator",
            "description": "A dynamic BMI calculator built using Streamlit.",
            "image": "https://via.placeholder.com/300x200?text=BMI+Calculator",
            "link": "https://share.streamlit.io/"
        },
        {
            "title": "Data Visualization App",
            "description": "A data visualization app built with Streamlit and Python.",
            "image": "https://via.placeholder.com/300x200?text=Data+Viz+App",
            "link": "https://share.streamlit.io/"
        }
    ]

    for proj in streamlit_projects:
        st.markdown(f"""
        <div class="project-card">
            <h3>{proj['title']}</h3>
            <img src="{proj['image']}" alt="{proj['title']} Screenshot">
            <p>{proj['description']}</p>
            <a href="{proj['link']}" target="_blank">View Project</a>
        </div>
        """, unsafe_allow_html=True)

# ---- Contact ----
elif page == "Contact":
    st.title("Contact Me")
    st.write("Feel free to reach out for collaborations or inquiries.")

    with st.form("contact_form"):
        name = st.text_input("Name", placeholder="Enter your name")
        email = st.text_input("Email", placeholder="Enter your email")
        message = st.text_area("Message", placeholder="Write your message here")
        submitted = st.form_submit_button("Send Message")

        if submitted:
            st.success(f"Thanks, {name}! Your message has been received.")

# ---- Socials ----
elif page == "Socials":
    st.title("Connect With Me")
    st.write("Check out my work and connect with me on the following platforms:")

    st.markdown("### 🔗 GitHub")
    st.markdown("[GitHub Repo](https://github.com/Syedabanog-1/Python-Streamlit-Advanced-Secure-Data-Encryption-System.git)")

    st.markdown("### 🚀 Streamlit App")
    st.markdown("[Streamlit Project](https://python-app-advanced-secure-data-encryption-system-kbfpro6u8wh4.streamlit.app/)")

# ---- Footer ----
st.markdown("---")
st.caption("Made with ❤️ by Syeda Gulzar Bano")
