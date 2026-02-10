import streamlit as st
from ui.modes.chat import render_chat_mode
from ui.modes.flow import render_flow_mode
from ui.modes.simulate import render_simulate_mode

def render_mode():
    mode = st.session_state.mode

    if mode == "Chat":
        render_chat_mode()
    elif mode == "Flow (Low-code)":
        render_flow_mode()
    elif mode == "Simulate":
        render_simulate_mode()
    else:
        st.info("Unknown mode")