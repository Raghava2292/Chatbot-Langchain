import streamlit as st

from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain.chat_models import ChatOpenAI

## Streamlit UI
st.set_page_config(page_title="Conversational Chatbot")
st.header("Hey! Let's Chat")

from dotenv import load_dotenv
load_dotenv()
import os

chat=ChatOpenAI(temperature=0.5)
tone = st.selectbox('Which tone should I have for this conversation?', ('Professional', 'Humourous', 'Serious'))

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages']=[
        SystemMessage(content=f'You are my AI assistant. Maintain {tone} for our conversation.')
    ]

## Function to load OpenAI model and get respones

def get_chatmodel_response(question):

    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer=chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content

input=st.text_input("Input: ",key="input")
response=get_chatmodel_response(input)

submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    st.subheader("Here's your answer")
    st.write(response)