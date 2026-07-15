
from dotenv import load_dotenv
load_dotenv()
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage
model=ChatMistralAI(model="mistral-small-2506",temperature=0.9)
print("-------welcome type0 to the application")
messages=[
    SystemMessage(content="you are a very funny ai agent")

]
while True:
       
       prompt=input("you: ")
       messages.append(HumanMessage(content=prompt))
       if prompt == "0":
        break
       response=model.invoke(messages)
       messages.append(AIMessage(content=response.content))


       print("Bot :",response.content)