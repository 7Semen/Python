from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.db import crud
from app.schemas import BookCreate, BookUpdate, BookResponse

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/", response_model=list[BookResponse])
def get_books(
    category_id: int | None = Query(default=None),
    db: Session = Depends(get_db)
):
    if category_id is not None:
        return crud.list_books_by_category(db, category_id)
    return crud.list_books(db)

@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    obj = crud.get_book(db, book_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Book not found")
    return obj

@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(payload: BookCreate, db: Session = Depends(get_db)):
    # проверка категории
    if not crud.get_category(db, payload.category_id):
        raise HTTPException(status_code=404, detail="Category not found")

    return crud.create_book(
        db,
        title=payload.title,
        description=payload.description,
        price=payload.price,
        url=payload.url,
        category_id=payload.category_id
    )

@router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: int, payload: BookUpdate, db: Session = Depends(get_db)):
    # если меняем category_id — проверить существование
    if payload.category_id is not None and not crud.get_category(db, payload.category_id):
        raise HTTPException(status_code=404, detail="Category not found")

    obj = crud.update_book(
        db,
        book_id,
        title=payload.title,
        description=payload.description,
        price=payload.price,
        url=payload.url,
        category_id=payload.category_id
    )
    if not obj:
        raise HTTPException(status_code=404, detail="Book not found")
    return obj

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_book(db, book_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Book not found")
    return
