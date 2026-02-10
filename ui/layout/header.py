import streamlit as st

def render_header():
    ss = st.session_state
    st.markdown(
        """
        <div class="ai-card">
          <div style="display:flex;justify-content:space-between;align-items:center;gap:12px;">
            <div>
              <div style="font-size:22px;font-weight:800;">AI Pilot: The Autonomous Entity</div>
              <div class="ai-muted">Build smarter. Ship faster. Power the next wave of AI.</div>
            </div>
            <div style="display:flex;gap:8px;flex-wrap:wrap;justify-content:flex-end;">
              <span class="ai-pill">UI/UX</span>
              <span class="ai-pill">Developer Tool</span>
              <span class="ai-pill">AI Innovation</span>
              <span class="ai-pill">Real-time Systems</span>
              <span class="ai-pill">Voice + Multimodal</span>
              <span class="ai-pill">Mood: %s</span>
            </div>
          </div>
        </div>
        """ % ss.mood,
        unsafe_allow_html=True,
    )
    st.write("")