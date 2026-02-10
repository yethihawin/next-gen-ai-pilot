import streamlit as st
import json

def render_flow_mode():
    st.markdown("#### 🧩 Flow (Low-code / Builder)")

    st.caption("Create a pseudo-flow that later becomes an agent workflow.")

    with st.form("flow_builder"):
        goal = st.text_input("Goal", placeholder="e.g., Voice → Transcript → Summarize → Create tasks")
        inputs = st.multiselect("Inputs", ["text", "voice", "file", "live"], default=["text"])
        outputs = st.multiselect("Outputs", ["chat", "cards", "charts", "status"], default=["chat", "charts"])
        steps = st.text_area("Steps (one per line)", placeholder="1) Capture input\n2) Extract entities\n3) Call agent\n4) Render charts")
        submitted = st.form_submit_button("Generate Flow JSON")

    if submitted:
        flow = {
            "goal": goal,
            "inputs": inputs,
            "outputs": outputs,
            "steps": [s.strip() for s in steps.splitlines() if s.strip()],
        }
        st.markdown("##### ✅ Flow JSON")
        st.code(json.dumps(flow, indent=2), language="json")
        st.info("Next: Hook this to Gradient workflow runner (later).")