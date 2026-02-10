import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from ui.app_state import init_state
from ui.styles.theme import apply_theme
from ui.layout.sidebar import render_sidebar
from ui.layout.header import render_header
from ui.layout.workspace import render_workspace

st.set_page_config(
    page_title="AI Pilot: The Autonomous Entity",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

def main():
    init_state()
    apply_theme()

    render_sidebar()
    render_header()
    render_workspace()

if __name__ == "__main__":
    main()