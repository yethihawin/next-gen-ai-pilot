import streamlit as st
from ui.components.copilot import render_copilot

def render_sidebar():
    ss = st.session_state
    with st.sidebar:
        st.markdown("### 🧠 AI Pilot")
        st.caption("Build smarter. Ship faster. Power the next wave of AI.")

        # Mode switch
        ss.mode = st.radio(
            "Mode",
            ["Chat", "Flow (Low-code)", "Simulate"],
            index=["Chat", "Flow (Low-code)", "Simulate"].index(ss.mode),
        )

        # Theme toggle
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🌙 Dark", use_container_width=True):
                ss.theme = "dark"
                st.rerun()
        with col2:
            if st.button("☀️ Light", use_container_width=True):
                ss.theme = "light"
                st.rerun()

        # Mood awareness
        ss.mood = st.selectbox(
            "AI Mood Awareness",
            ["Focused", "Calm", "Creative", "Urgent"],
            index=["Focused", "Calm", "Creative", "Urgent"].index(ss.mood),
            help="UI accent + suggestions will adapt to mood.",
        )

        st.markdown("---")

        # Model status box
        status = ss.model_status
        st.markdown(
            f"""
            <div class="ai-card">
              <div><b>Model Status</b></div>
              <div class="ai-muted">State: <span class="ai-accent"><b>{status["state"]}</b></span></div>
              <div class="ai-muted">Latency: {status["latency_ms"] or "—"} ms</div>
              <div class="ai-muted">Last ping: {status["last_ping"] or "—"}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("---")
        render_copilot()