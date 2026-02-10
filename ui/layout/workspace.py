import streamlit as st
from ui.modes.router import render_mode
from ui.components.charts import render_realtime_charts

def render_workspace():
    left, right = st.columns([2.2, 1], gap="large")

    with left:
        render_mode()

    with right:
        render_realtime_charts()