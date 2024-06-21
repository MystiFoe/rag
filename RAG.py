
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain

# For openai key
import os
os.environ["OPENAI_API_KEY"] = "Your Key"

# load a PDF  
loader = PyPDFLoader("/content/qlora_paper.pdf")
documents = loader.load()