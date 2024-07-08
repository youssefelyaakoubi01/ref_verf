from langchain_core.prompts import PromptTemplate
import fitz
from serializers.nlp_traitement import get_text_after_word
from langchain_groq import ChatGroq
from langchain.output_parsers.json import SimpleJsonOutputParser
import json
path_aticles= "./data/"

model = ChatGroq(
        model="mixtral-8x7b-32768",
        api_key="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",
        temperature=0 )

json_prompt = PromptTemplate.from_template(
    """ 
        À partir de ce texte {text},retourner une seule référence au format JSON comme le format suivant : "titreArticle":string,"auteurs": ["nom_complet":string ] 
    """
)
json_parser = SimpleJsonOutputParser()

def extract_text_from_pdf(file_path: str) -> str:
    """
    Extrait le texte d'un fichier PDF donné.

    :param file_path: Le chemin du fichier PDF.
    :return: Le texte extrait du fichier PDF.
    """
    # Ouvrir le document PDF
    pdf_document = fitz.open(file_path)
    
    # Extraire le texte de chaque page du PDF
    text = ""
    for page in pdf_document:
        text += page.get_text()
    
    return text


def verify_article(file_path):
    # Extraire le texte 
    text = extract_text_from_pdf(file_path)
    print(text)
    references=get_text_after_word(text)
    print(references)
    json_chain = json_prompt | model | json_parser
    reponse=json_chain.invoke({'text':references})
    
    print(reponse['titreArticle'])
    
    
