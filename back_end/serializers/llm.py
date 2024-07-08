from groq import Groq
from langchain_groq import ChatGroq
from rag.chercher_similartite import fun_chercher_similarite
from dotenv import load_dotenv
load_dotenv()
import os
from fastapi import UploadFile,File

GROQ_API_KEY = os.getenv('GROQ_API_KEY')


client = ChatGroq(
        model="llama3-70b-8192",
        api_key="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",
        temperature=0.5 )

def ask_llm(question):
    full_prompt = fun_chercher_similarite(question)
    reponse = client.invoke(full_prompt).content
    print(reponse)
    return reponse

def chat_llm(question):
        reponse = client.invoke("'system:','Essayer de répondre à la question après avoir la dérinière answer de la conversation!' " + question).content
        print(reponse)
        return reponse



