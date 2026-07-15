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
st.markdown("""
<p style='text-align:center;
color:white;
font-size:18px;'>
Find your next binge-worthy show 🍿
</p>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* Background */
.stApp{
    background-color:#000000;
}

/* Hide Streamlit branding */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Title */
h1{
    color:#E50914 !important;
    text-align:center;
    font-size:50px !important;
    font-weight:bold;
}

/* All text */
h2,h3,h4,h5,h6,p,label,span{
    color:white !important;
}

/* Chat input */
.stChatInput input{
    background:#111111 !important;
    color:white !important;
    border:2px solid #E50914 !important;
    border-radius:12px !important;
}

/* Text input */
.stTextInput input{
    background:#111111 !important;
    color:white !important;
    border:2px solid #E50914 !important;
    border-radius:12px !important;
}

/* Placeholder */
.stTextInput input::placeholder,
.stChatInput input::placeholder{
    color:#cccccc !important;
}

/* Button */
.stButton>button{
    background:#E50914 !important;
    color:white !important;
    border:none !important;
    border-radius:10px !important;
    padding:12px 25px !important;
    font-size:18px !important;
    font-weight:bold !important;
    width:100%;
}

.stButton>button:hover{
    background:#B20710 !important;
}

/* Chat messages */
.stChatMessage{
    background:#181818 !important;
    border-left:5px solid #E50914;
    border-radius:12px;
    padding:12px;
    margin-bottom:10px;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#0a0a0a;
}

section[data-testid="stSidebar"] *{
    color:white !important;
}

/* Markdown */
div[data-testid="stMarkdownContainer"]{
    color:white !important;
}

/* Success, Error, Warning */
.stSuccess,.stWarning,.stError{
    color:white !important;
}

/* Scrollbar */
::-webkit-scrollbar{
    width:8px;
}

::-webkit-scrollbar-thumb{
    background:#E50914;
    border-radius:10px;
}

::-webkit-scrollbar-track{
    background:#000000;
}

</style>
""", unsafe_allow_html=True)

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
    st.markdown(f"""
<div style="
background:#181818;
padding:20px;
border-radius:12px;
border-left:5px solid #E50914;
margin-top:15px;
">
<h3 style="color:#E50914;">🍿 Recommended Shows</h3>
<p style="color:white;">{response}</p>
</div>
""", unsafe_allow_html=True)

    st.session_state.messages.append(
        AIMessage(content=response.content)
    )

    # Show AI response
    with st.chat_message("assistant"):
        st.write(response.content)