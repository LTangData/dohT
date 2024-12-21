from typing import List

import streamlit as st

from UI.pages.database_login import login
from UI.pages.query_executor import query
from config.ui_config import STYLES_DIR


st.set_page_config(
    page_title="Get Rid of Query"
)

def load_css(*files: List[str]) -> None:
    """
    Loads CSS from a specified file into a Streamlit application.

    This function reads the contents of a CSS file and injects it into the Streamlit app as a style tag. This allows for custom styling of the Streamlit app directly from an external CSS file.

    Args:
        file_name (str): The path to the CSS file to be loaded.

    Raises:
        FileNotFoundError: If the CSS file does not exist at the specified path.
    """
    try:
        css_content = ""
        for file in files:
            with open(file, "r") as f:
                css_content += f.read() + "\n"
        st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file} does not exist.")

# Database credentials input
if "db_info" not in st.session_state:
    st.session_state["db_info"] = {}

current_page = st.query_params.get("page", "login")

if current_page == "login":
    login()
    load_css(f"{STYLES_DIR}/base.css", f"{STYLES_DIR}/login.css")
elif current_page == "query":
    query()
    load_css(f"{STYLES_DIR}/base.css", f"{STYLES_DIR}/query.css")
else:
    st.error("Page not found.")