from fastapi import FastAPI, requests
from routes.user import user_root
from routes.llm import llm_root
from routes.article import article_root
from rag.populate_database import  embedding_main
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Mettez votre domaine Angular ici
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(user_root)
app.include_router(llm_root)
app.include_router(article_root)

@app.get('/')
async def redirect():
    return RedirectResponse("/docs")


@app.post('/embedding')
def embedding():
    return embedding_main
