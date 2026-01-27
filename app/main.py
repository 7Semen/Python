from fastapi import FastAPI
from app.api import books, categories

app = FastAPI()

app.include_router(categories.router)
app.include_router(books.router)

@app.get("/health")
def health():
    return {"status": "ok"}
