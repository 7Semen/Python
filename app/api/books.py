from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.db import crud
from app.schemas import BookCreate, BookResponse

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/", response_model=list[BookResponse])
def get_books(category_id: int | None = None, db: Session = Depends(get_db)):
    return crud.get_books(db, category_id)

@router.post("/", response_model=BookResponse, status_code=201)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)
