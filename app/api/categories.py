from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.db import crud
from app.schemas import CategoryCreate, CategoryResponse

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("/", response_model=list[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)

@router.post("/", response_model=CategoryResponse, status_code=201)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category)
