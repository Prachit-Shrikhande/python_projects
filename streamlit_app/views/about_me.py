import streamlit as st
from forms.contact import contact_form


@st.dialog("Contact Me")
def show_contact_form():
    contact_form()
    

col1, col2 = st.columns(2 , gap="small", vertical_alignment="center")

with col1:
    st.image("./assets/profile.jpeg", width=230)
with col2:
    st.title("Prachit Shrikhande", anchor=False)
    st.write("""
             Aspiring Software Engineer with a comprehensive background in Full Stack Development and DevOps, seeking opportunities to leverage expertise in Angular, Python, MySQL, and Java. Eager to contribute to innovative projects, draw on extensive experience in system maintenance, and apply technical proficiencies in backend and front-end technologies for impactful contributions to dynamic teams.
    """)
    if st.button("Contact Me"):
        show_contact_form()


st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - 3 Years experience Working as a Software Engineer with Full Stack Developer and Devops responsibilities while contributing in developing and maintaining deliverable projects using Angular, Python, MySQL and Java.
    - Strong hands-on knowledge and experience in Python and Angular
    - Good understanding of Web and ML application deployment and respective tools.
    - Work experience on Big Data Technologies
    """
)

st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Data Science: Numpy, Pandas, PyTorch, Tensorflow, NLP, NER, Matplotlib, OpenCV
    - Big Data Technologies: Azure Databricks, Hadoop, Pandas, Spark/PySpark, Hive, Snowflake, MySQL, Oracle SQL, Postgres SQL
    - Front-end Technologies: HTML, CSS, Angular
    - Backend Technologies: Python (FastAPI), Java (Spring Boot)
    - Other Technologies: Linux (ssh), Python/Bash scripting, Docker, AWS, Jenkins, Nginx Server, Grafana (server monitoring tool), Git, Gitlab
    """
)