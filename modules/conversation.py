from langchain.chat_models import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template
from langchain.llms import HuggingFaceHub


def get_conversational_chain(vector_store):
    llm = HuggingFaceHub(model_id="hkunlp/instructor-xl")
    memory = ConversationBufferMemory(
        memory_key="chat_history", return_messages=True)

    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        memory=memory,
        retriever=vector_store.as_retriever(),
    )

    return chain
