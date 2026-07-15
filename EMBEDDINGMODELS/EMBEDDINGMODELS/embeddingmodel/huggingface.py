from langchain_huggingface import HuggingFaceEmbeddings
embedding=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
texts=[
    "hello this is akash viyas"
    "hello your name is youtube"
    "and you are very beautiful"
]
vector=embedding.embed_documents(texts)
print(vector)