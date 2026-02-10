import streamlit as st
from ui.integrations.gradient import call_agent, ping_model

def _extract_answer(result: dict) -> str:
    """Try to extract assistant text from OpenAI-style response."""
    try:
        return result["choices"][0]["message"]["content"]
    except Exception:
        # fallback for debug
        return result.get("output") or result.get("result") or str(result)

def render_chat_mode():
    st.markdown("#### 💬 Chat (Voice + Text + File)")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🔌 Connect / Ping Model", use_container_width=True):
            ping_model()
            st.rerun()
    with col2:
        st.caption("Tip: Use Copilot suggestions in sidebar.")

    text = st.text_area("Text input", placeholder="Ask anything…", height=120)

    send = st.button("🚀 Send", use_container_width=True)

    # Show history
    if "chat" not in st.session_state:
        st.session_state.chat = []

    for msg in st.session_state.chat:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if send:
        if not text.strip():
            st.warning("Please enter text.")
            return

        st.session_state.chat.append({"role": "user", "content": text})

        with st.chat_message("assistant"):
            with st.spinner("Thinking…"):
                result = call_agent(text)
                answer = _extract_answer(result)
                st.markdown(answer)

        st.session_state.chat.append({"role": "assistant", "content": answer})
        st.rerun()