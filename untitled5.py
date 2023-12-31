# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/165uixaRTCqT8xM5Rjsv0PkhJ0CRtxDd0
"""

pip install openai

pip install streamlit

pip install streamlit-chat

import streamlit as st
import openai
from streamlit_chat import message
openai.api_key = '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'

def api_calling(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message
    st.title("ChatGPT ChatBot With Streamlit and OpenAI")
if 'user_input' not in st.session_state:
    st.session_state['user_input'] = []

if 'openai_response' not in st.session_state:
    st.session_state['openai_response'] = []

def get_text():
    input_text = st.text_input("write here", key="input")
    input_text=input('enter')
    return input_text

user_input = get_text()

if user_input:
    output = api_calling(user_input)
    output = output.lstrip("\n")

    # Store the output
    st.session_state.openai_response.append(user_input)
    st.session_state.user_input.append(output)

message_history = st.empty();

if st.session_state.get('user_input'):

    for i in range(len(st.session_state['user_input']) - 1, -1, -1):
        # This function displays user input
        message(st.session_state["user_input"][i],
                key=str(i), avatar_style="icons")
        # This function displays OpenAI response
        message(st.session_state['openai_response'][i],
                avatar_style="miniavs", is_user=True , key=str(i) + 'data_by_user')





import openai
import streamlit as st

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="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", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

if "messages" in st.session_state:  # Checking if "messages" exists in session_state
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    openai.api_key = openai_api_key
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)

