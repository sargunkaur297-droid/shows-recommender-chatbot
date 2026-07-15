from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
load_dotenv()
print(os.getenv("OPENAI_API_KEY"))
embeddings=OpenAIEmbeddings(
    model='text-embedding-3-large',
    dimensions=64
)

vector = embeddings.embed_query("you are going to learn genai")
print(vector)