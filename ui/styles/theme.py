import streamlit as st

MOOD_ACCENT = {
    "Focused": "#4F46E5",   # indigo
    "Calm": "#06B6D4",      # cyan
    "Creative": "#F59E0B",  # amber
    "Urgent": "#EF4444",    # red
}

def apply_theme():
    ss = st.session_state
    accent = MOOD_ACCENT.get(ss.mood, "#4F46E5")

    if ss.theme == "dark":
        bg = "#0B1220"
        panel = "#111B2E"
        text = "#E5E7EB"
        muted = "#9CA3AF"
        border = "rgba(255,255,255,0.08)"
    else:
        bg = "#F7F8FB"
        panel = "#FFFFFF"
        text = "#111827"
        muted = "#6B7280"
        border = "rgba(0,0,0,0.08)"

    st.markdown(
        f"""
        <style>
        .stApp {{
            background: {bg};
            color: {text};
        }}
        .ai-card {{
            background: {panel};
            border: 1px solid {border};
            border-radius: 14px;
            padding: 14px 16px;
        }}
        .ai-muted {{ color: {muted}; }}
        .ai-accent {{ color: {accent}; }}
        .ai-pill {{
            display: inline-block;
            padding: 4px 10px;
            border-radius: 999px;
            border: 1px solid {border};
            background: rgba(79,70,229,0.10);
            color: {text};
            font-size: 12px;
        }}
        .ai-btn {{
            border-radius: 12px !important;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )