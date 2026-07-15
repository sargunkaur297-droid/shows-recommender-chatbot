from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct"
)
model=ChatHuggingFace(llm=llm)
response = model.invoke("who are you?")
print(response.content)