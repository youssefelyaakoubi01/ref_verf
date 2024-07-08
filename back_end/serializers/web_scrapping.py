import requests
import json


titre_Article_ex= "Testing+of+Detection+Tools+for+AI-Generated+Text"
auteurs_ex= "Weber-Wulff+D,+Anohina-Naumeca+A,+Bjelobaba+S,+Foltýnek+T,+Guerrero-Dib+J,+Popoola+O,+et+al"
api_key = '7461b977d36daab11d7f78fb8f3e893d8a64b07172ca63148c4d20e70c5a2cd6'
def verifyRef(titre_Article,auteurs):

    r = requests.get(f'https://serpapi.com/search.json?engine=google_scholar&q={titre_Article}&as_sathors="{auteurs}"&api_key={api_key}')
    print(r.text)
    
    result=json.loads(r.text)
    
    titreArticleRecu=result['organic_results'][0]['title']
    print(titreArticleRecu)
    authors_names= []
    for author in result['organic_results'][0]['publication_info']['authors']:
     authors_names.append(author['name'])
    print("Les auteurs sont:",authors_names)


    nombre_cite = result['organic_results'][0]['inline_links']['cited_by']['total']
    print(f"le nombre de citation pour l'artice avec le titre cité dans les référence est:",nombre_cite)