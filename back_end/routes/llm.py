from fastapi import APIRouter,UploadFile,File
from serializers.llm import ask_llm,chat_llm
from serializers.llm_ar import ask_llm_arabic
llm_root = APIRouter()

@llm_root.get('/ask-smart-judge/{question}')
def pose_question(question):
    return ask_llm(question)

@llm_root.get('/ask-smart-judge/chatbot/{question}')
def pose_question(question):
    return chat_llm(question)
    
@llm_root.get('/ask-smart-judge/chatbot_ar/{question}')
def llm_arabic(question):
    return ask_llm_arabic(question)


