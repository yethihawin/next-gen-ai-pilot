import streamlit as st
import random

def render_simulate_mode():
    st.markdown("#### 🎮 Simulate (Agent Playground)")

    scenario = st.selectbox(
        "Scenario",
        ["Incident Response", "Product Sprint", "Customer Support", "Research Assistant"],
    )

    difficulty = st.slider("Difficulty", 1, 10, 5)

    if st.button("▶ Run Simulation", use_container_width=True):
        score = random.randint(40, 95) - difficulty
        score = max(0, min(100, score))
        st.success(f"Simulation complete. Agent score: **{score}/100**")
        st.write("Next: connect to real agent reasoning + telemetry.")