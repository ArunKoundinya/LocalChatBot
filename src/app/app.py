# app.py

import sys
import os
import streamlit as st
import configparser

# Ensure module resolution works correctly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.myagent.langchain_agent import ChatBotEngine
from src.utils.utils import apply_styles

config = configparser.ConfigParser()
config.read('src/myagent/models_prompts.ini')

botname = config.get('names', 'name')
username = config.get('names', 'username')

# Page setup
st.set_page_config(page_title=f"💬 Chat with {botname}", page_icon="💖")
st.title(f"💬 Chat with {botname}")
st.markdown("Talk to your AI girlfriend 💁‍♀️")

# Initialize session state
if "chatbot" not in st.session_state:
    st.session_state.chatbot = ChatBotEngine()
if "history" not in st.session_state:
    st.session_state.history = []
if "input" not in st.session_state:
    st.session_state.input = ""

# Callback to handle message sending
def handle_send():
    user_input = st.session_state.input.strip()
    if user_input:
        response = st.session_state.chatbot.ask(user_input)
        st.session_state.history.append((f"{username}", user_input))
        st.session_state.history.append((f"{botname}", response))
        st.session_state.input = ""  # Clear the input field

# Apply custom styles
apply_styles()

# Display chat history in a scrollable container
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for speaker, text in st.session_state.history:
    if speaker == username:
        st.markdown(f"**🧔 {username}:** {text}")
    else:
        st.markdown(f"**💁‍♀️ {botname}:** {text}")
st.markdown('</div>', unsafe_allow_html=True)

# Display the input box at the bottom (fixed position)
st.markdown('<div class="input-container">', unsafe_allow_html=True)
st.text_input("You:", key="input", on_change=handle_send)
st.markdown('</div>', unsafe_allow_html=True)
