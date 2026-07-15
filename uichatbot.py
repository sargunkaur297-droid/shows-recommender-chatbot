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
<style>

/* Google Font */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

/* Whole App */
html, body, [class*="css"]{
    font-family: 'Poppins', sans-serif;
}

.stApp{
    background-color:#141414;
    color:white;
}

/* Hide Streamlit Menu & Footer */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Title */
h1{
    color:#E50914 !important;
    text-align:center;
    font-size:48px !important;
    font-weight:700 !important;
}

h2,h3,h4,h5,h6{
    color:white !important;
}

/* Normal Text */
p,label,span{
    color:white !important;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#0B0B0B;
}

/* Text Input */
.stTextInput input{
    background:#222222;
    color:white;
    border:2px solid #E50914;
    border-radius:12px;
    padding:12px;
}

.stTextInput input:focus{
    border:2px solid #E50914;
    box-shadow:0 0 10px #E50914;
}

/* Text Area */
textarea{
    background:#222222 !important;
    color:white !important;
    border-radius:12px !important;
}

/* Button */
.stButton>button{
    width:100%;
    background:#E50914;
    color:white;
    border:none;
    border-radius:12px;
    padding:12px;
    font-size:18px;
    font-weight:600;
    transition:0.3s;
}

.stButton>button:hover{
    background:#B20710;
    transform:scale(1.02);
}

/* Select Box */
.stSelectbox div[data-baseweb="select"]{
    background:#222222;
    color:white;
}

/* Slider */
.stSlider{
    color:#E50914;
}

/* Chat Messages */
.stChatMessage{
    background:#1F1F1F;
    border-radius:15px;
    padding:15px;
    border-left:5px solid #E50914;
    margin-bottom:12px;
}

/* Markdown Blocks */
div[data-testid="stMarkdownContainer"]{
    color:white;
}

/* Code Block */
pre{
    background:#222222 !important;
    color:white !important;
    border-radius:10px;
}

/* Success Message */
.stSuccess{
    background:#1F1F1F !important;
    color:white !important;
}

/* Warning */
.stWarning{
    background:#332700 !important;
    color:white !important;
}

/* Error */
.stError{
    background:#3B0A0A !important;
    color:white !important;
}

/* Recommendation Card */
.card{
    background:#1F1F1F;
    padding:20px;
    border-radius:15px;
    border-left:5px solid #E50914;
    box-shadow:0px 0px 15px rgba(229,9,20,0.3);
    margin-top:20px;
}

/* Scrollbar */
::-webkit-scrollbar{
    width:8px;
}

::-webkit-scrollbar-track{
    background:#141414;
}

::-webkit-scrollbar-thumb{
    background:#E50914;
    border-radius:10px;
}

::-webkit-scrollbar-thumb:hover{
    background:#B20710;
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

    st.session_state.messages.append(
        AIMessage(content=response.content)
    )

    # Show AI response
    with st.chat_message("assistant"):
        st.write(response.content)