from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import os
token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
print("Token loaded:", bool(token))