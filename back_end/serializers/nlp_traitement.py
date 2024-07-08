import spacy


#importer notre modele anglais
nlp = spacy.load('en_core_web_lg')
word = "References"
def get_text_after_word(text):
    # Traiter le texte avec SpaCy
    doc = nlp(text)
    # Chercher le mot dans le texte
    for token in doc:
        if token.text.lower() == word.lower():
            # Récupérer le texte après le mot
            return text[token.idx + len(token.text):]
    return ""
