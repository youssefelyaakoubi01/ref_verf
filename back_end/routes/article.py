from fastapi import APIRouter, File, UploadFile
from serializers.article import verify_article
article_root = APIRouter()
import json
path_aticles= "./data/"
@article_root.post('/verify_article/ref')
async def verify_article_(file: UploadFile = File(...)):
    content = await file.read()
    with open(f"{path_aticles}{file.filename}","wb") as f:
        f.write(content)
    article = {"filename":file.filename, "path":f"{path_aticles}{file.filename}"}
    print("l'article a bien enregistré!" )
    return verify_article(article["path"])