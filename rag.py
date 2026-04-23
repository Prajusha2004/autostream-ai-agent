from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import TextLoader

loader = TextLoader("data.txt")
docs = loader.load()

db = FAISS.from_documents(docs, OpenAIEmbeddings())

def retrieve(query):
    return db.similarity_search(query, k=2)