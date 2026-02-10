import streamlit as st
import time
import random

def render_realtime_charts():
    ss = st.session_state
    st.markdown("#### 📈 Real-time Charts & Status")

    st.markdown(
        """
        <div class="ai-card">
          <div><b>Live Metrics</b></div>
          <div class="ai-muted">Token usage, latency, and model health (demo)</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")

    # Simple live chart demo
    chart_placeholder = st.empty()

    if st.button("🔄 Update Live Chart", use_container_width=True):
        # Update session chart data
        ss.live_chart_data = ss.live_chart_data[-20:] + [ss.live_chart_data[-1] + random.randint(-3, 5)]
        chart_placeholder.line_chart(ss.live_chart_data)

    # Show once even without click
    chart_placeholder.line_chart(ss.live_chart_data)

    st.write("")
    st.markdown("##### ✅ Model Snapshot")
    st.json(ss.model_status)
