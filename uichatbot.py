import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# Load environment variables
load_dotenv()

# Create model
model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.9
)

st.set_page_config(page_title="Funny AI Chatbot", page_icon="🤖")

st.title("🤖 shows recommender")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a movie and webseries expert.Recommend titles based on the user's preferences and briefly explain why they might enjoy them.")
    ]

# Display previous messages
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.write(message.content)

# User input
prompt = st.chat_input("Type your message...")

if prompt:

    # Show user message
    with st.chat_message("user"):
        st.write(prompt)

    st.session_state.messages.append(HumanMessage(content=prompt))

    # Get response
    response = model.invoke(st.session_state.messages)

    st.session_state.messages.append(
        AIMessage(content=response.content)
    )

    # Show AI response
    with st.chat_message("assistant"):
        st.write(response.content)