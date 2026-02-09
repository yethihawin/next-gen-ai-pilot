import streamlit as st
import requests

# Page Title
st.set_page_config(page_title="Next-Gen AI Pilot", page_icon="🚀")
st.title("🚀 Next-Gen AI Pilot")
st.subheader


API_KEY = "wD74M1A43hyrpWFbiIvnybY2Jb_f_V-y"
ENDPOINT = "https://ouys56vfsjl6w4ud6huas3yn.agents.do-ai.run/v1/chat/completions"

# Chat history 
if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User ဆီက စာလက်ခံဖို့
if prompt := st.chat_input("Next-Gen AI ကို တစ်ခုခု မေးကြည့်ပါ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI ဆီက အဖြေတောင်းဖို့
    with st.chat_message("assistant"):
        headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
        payload = {
            "model": "OpenAI GPT-oss-120b", # သင့် Model ID
            "messages": st.session_state.messages
        }
        
        try:
            response = requests.post(ENDPOINT, headers=headers, json=payload)
            full_response = response.json()['choices'][0]['message']['content']
            st.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
        except Exception as e:
            st.error(f"Error: {e}")
