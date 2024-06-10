import streamlit as st
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import HuggingFaceHub
from templates.html_template import css, bot_template, user_template


def get_conversational_chain(vector_store):
    llm = HuggingFaceHub(repo_id="CohereForAI/aya-101",
                         model_kwargs={"temperature": 0.5, "max_length": 512})
    memory = ConversationBufferMemory(
        memory_key="chat_history", return_messages=True)

    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        memory=memory,
        retriever=vector_store.as_retriever(),
    )

    return chain


def handle_user_question(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for index, message in enumerate(st.session_state.chat_history):
        if index % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
