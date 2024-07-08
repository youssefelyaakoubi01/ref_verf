from langchain.vectorstores.chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from rag_arabe.get_embedding_function_m import get_embedding_function
import time

CHROMA_PATH = "./chroma_ar"

# Configurer Template Prompt
prompt_template= ChatPromptTemplate.from_messages(
    [
       # ("system", "Vous êtes un Smart Review qui évalué les articles scientifiques,votre spécialité de vérifier les références citées à partir de la base de données, et de citer les références existantes, non existantes. Votre nom est: {name}."),
      
        ("system", "Répondre en arabe, Vous êtes un Smart Reveiw  qui évalue les articles scientifiques.ne dire pas consulter un expert, voici la question {question}  "),
        ("human","Basée sur le contexte suivant {context} ")
    ]
)


def fun_chercher_similarite(question):
    # Prepare the DB.
    print("\n **************** Début  de péreparation de base de données !'  ******************\n ")
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
    print("\n **************** Fin  de péreparation de base de données !'  ******************\n\n ")

    # Search the DB.
    print(" **************** Début  D'opération 'Chercher dans la base de données (ChromaDB) !'  ******************\n ")
    results = db.similarity_search_with_score(question, k=15)
    if len(results) == 0:
        print("Désolé,La réponse de votre question n'existe pas dans la base de donées :( , essayer de poser une autre question!")
    print("**************** Fin  D'opération 'Chercher dans la base de données (ChromaDB) !'  ******************\n ")

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt = prompt_template.format(context=context_text, question=question)
    print(prompt)
    return prompt