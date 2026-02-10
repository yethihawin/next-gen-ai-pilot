import streamlit as st

MOOD_SUGGESTIONS = {
    "Focused": [
        "Convert chat into tasks & checklist",
        "Generate deployment steps for Gradient App",
        "Summarize with bullet points + next actions",
    ],
    "Calm": [
        "Create a gentle onboarding tutorial for new users",
        "Simplify UI labels and reduce clutter",
        "Generate concise status summary",
    ],
    "Creative": [
        "Propose 3 new features for multimodal agent",
        "Design a futuristic UI concept",
        "Create a hackathon demo script (3 minutes)",
    ],
    "Urgent": [
        "Incident response: triage and action plan",
        "Fast debug checklist for endpoint failures",
        "Generate quick MVP scope for shipping today",
    ],
}

def render_copilot():
    ss = st.session_state
    st.markdown("### 🧭 Copilot")
    st.caption("Suggestions adapt to mood.")

    suggestions = MOOD_SUGGESTIONS.get(ss.mood, ss.copilot_suggestions)

    for s in suggestions:
        if st.button(f"➕ {s}", use_container_width=True):
            # Put suggestion into chat input as a message shortcut
            ss.chat.append({"role": "user", "content": f"[Copilot Suggestion]\n{s}"})
            st.rerun()
