import streamlit as st
import pandas as pd

about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)

project_1_page = st.Page(
    page="views/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)

pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page],
    }
)

pg.run()