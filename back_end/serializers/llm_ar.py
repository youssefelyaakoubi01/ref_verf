
from groq import Groq
from langchain_groq import ChatGroq
from rag_arabe.chercher_similartite import fun_chercher_similarite






client = ChatGroq(
        model="llama3-70b-8192",
        api_key="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",
        temperature=1 )


def ask_llm_arabic(question):
    full_prompt = fun_chercher_similarite(question)
    reponse = client.invoke(full_prompt).content
    print(reponse)
    return reponse
