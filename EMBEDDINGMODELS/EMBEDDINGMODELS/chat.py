

from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
load_dotenv()

model = ChatMistralAI(model = "mistral-small-2506",temperature=0,max_tokens=20)

response=model.invoke("give me a joke on machine")

print(response.content)

