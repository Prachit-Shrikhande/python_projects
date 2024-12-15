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
            I’m a passionate and driven Software Engineer with over 3 years of experience building and maintaining software solutions that make a difference. With a strong foundation in Full Stack Development, DevOps, and Big Data Technologies, I love solving problems, learning new things, and contributing to impactful projects.
    """)
    # if st.button("Contact Me"):
    #     show_contact_form()


st.write("\n")
st.subheader("What I Bring to the Table:", anchor=False)
st.write(
    """
    - Hands-On Development Experience: I’ve worked extensively with Angular, Python, Java, and MySQL to create robust, scalable applications. Whether it’s crafting the front-end or optimizing the back-end, I ensure everything works seamlessly.
    - DevOps Know-How: From setting up CI/CD pipelines to containerizing applications with Docker and managing deployments on AWS, I’ve streamlined workflows to make development smoother and faster.
    - Big Data Skills: I’ve tackled large datasets using tools like Azure Databricks, Hadoop, and Spark, uncovering insights and improving system performance.
    - A Love for Learning: I’m always exploring new technologies, whether it’s diving into Machine Learning with TensorFlow and PyTorch or experimenting with NLP for real-world applications.
    """
)

st.write("\n")
st.subheader("Skills I'm Proud of:", anchor=False)
st.write(
    """
    - Frontend: HTML, CSS, Angular
    - Backend: Python (FastAPI), Java (Spring Boot)
    - Big Data: SQL (MySQL, OracleSQL), Spark, Hadoop, Hive, Snowflake, Databricks
    - DevOps: Docker, Jenkins, AWS, Linux, Nginx
    - Data Science Tools: Numpy, Pandas, PyTorch, OpenCV
    - Scripting: Python, Bash
    """
)

st.write("\n")
st.subheader("What Drives Me:", anchor=False)
st.write(
    """
    I’m not just about the code—I care deeply about the impact of what I build. Whether it’s simplifying a process, solving a user’s pain point, or contributing to a bigger mission, I’m all in. I thrive in collaborative environments, where ideas are shared, and challenges are tackled together.
    """
)

st.write("\n")
st.subheader("Let's Connect!:", anchor=False)
st.write(
    """
    I’m excited to take on new challenges, contribute to meaningful projects, and grow as part of a dynamic team. If you’re looking for someone who’s dedicated, adaptable, and eager to make a difference, I’d love to chat!
    """
)

colu1, colu2, colu3 = st.columns([1, 1, 1]) 

with colu2:
    if st.button("Contact Me"):
        show_contact_form()