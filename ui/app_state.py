import streamlit as st

DEFAULT_SUGGESTIONS = [
    "Summarize my notes into action items",
    "Generate a deployment checklist for Gradient App",
    "Create a low-code flow for 'Voice → Transcript → Agent → Chart'",
    "Show current model status and token usage hints",
]

def init_state():
    ss = st.session_state

    if "theme" not in ss:
        ss.theme = "dark"  # "dark" or "light"

    if "mood" not in ss:
        ss.mood = "Focused"  # Focused/Calm/Creative/Urgent

    if "mode" not in ss:
        ss.mode = "Chat"

    if "model_status" not in ss:
        ss.model_status = {
            "state": "Disconnected",
            "latency_ms": None,
            "last_ping": None,
        }

    if "copilot_suggestions" not in ss:
        ss.copilot_suggestions = DEFAULT_SUGGESTIONS

    if "chat" not in ss:
        ss.chat = []  # list of {"role": "user"/"assistant", "content": str}

    if "live_chart_data" not in ss:
        ss.live_chart_data = [10, 12, 9, 14, 15]