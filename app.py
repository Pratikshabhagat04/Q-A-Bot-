
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
import streamlit as st

llm = ChatGroq(
    model="openai/gpt-oss-120b"
)

if "messages" not in st.session_state:
    st.session_state.messages=[]

###########################  UI Part ###############################

st.subheader("🤖AI Q&A Chatbot")


for msg in st.session_state.messages:
    st.chat_message(msg.get("role")).markdown(msg.get("content"))



query=st.chat_input("Ask Anything ......")
if query:
    
    
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").markdown(query)

    res = llm.invoke(st.session_state.messages)


    st.session_state.messages.append({"role": "assistant", "content": res.content})
    st.chat_message("user").markdown(res.content)

print(st.session_state.messages)






