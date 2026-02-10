import os
import time
import streamlit as st
import requests

def _get_env(name, default=""):
    return os.getenv(name, default).strip()

def call_agent(user_text: str):
    """
    DigitalOcean Agent Endpoint invocation:
    POST {AGENT_ENDPOINT}/api/v1/chat/completions
    Body: OpenAI-compatible 'messages' list
    """
    base_url = _get_env("DO_AGENT_URL")
    key = _get_env("DO_AGENT_KEY")

    if not base_url or not key:
        return {"error": "Missing DO_AGENT_URL / DO_AGENT_KEY in environment variables"}

    url = base_url.rstrip("/") + "/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
    }

    payload = {
        "messages": [
            {"role": "user", "content": user_text}
        ],
        "stream": False,
        # Optional debug/trace info (DigitalOcean supports these flags)
        "include_functions_info": True,
        "include_retrieval_info": True,
        "include_guardrails_info": True,
    }

    try:
        r = requests.post(url, headers=headers, json=payload, timeout=90)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e), "url": url}

def ping_model():
    """
    Simple ping using same endpoint.
    """
    t0 = time.time()
    res = call_agent("ping")
    latency = int((time.time() - t0) * 1000)

    ok = "error" not in res
    st.session_state.model_status = {
        "state": "Connected" if ok else "Disconnected",
        "latency_ms": latency if ok else None,
        "last_ping": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
def ping_model():
    """Simple connectivity test using same endpoint."""
    res = call_agent("ping")
    ok = "error" not in res
    st.session_state.model_status = {
        "state": "Connected" if ok else "Disconnected",
        "latency_ms": None,
        "last_ping": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
