from sqlalchemy.orm import Session
from sqlalchemy import select

from app.db import models

# ---------- Categories ----------
def list_categories(db: Session):
    return db.execute(select(models.Category)).scalars().all()

def get_category(db: Session, category_id: int):
    return db.get(models.Category, category_id)

def create_category(db: Session, title: str):
    obj = models.Category(title=title)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def update_category(db: Session, category_id: int, title: str):
    obj = get_category(db, category_id)
    if not obj:
        return None
    obj.title = title
    db.commit()
    db.refresh(obj)
    return obj

def delete_category(db: Session, category_id: int):
    obj = get_category(db, category_id)
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True

def get_category_by_title(db: Session, title: str):
    return db.query(models.Category).filter(models.Category.title == title).first()

# ---------- Books ----------
def list_books(db: Session):
    return db.execute(select(models.Book)).scalars().all()

def list_books_by_category(db: Session, category_id: int):
    stmt = select(models.Book).where(models.Book.category_id == category_id)
    return db.execute(stmt).scalars().all()

def get_book(db: Session, book_id: int):
    return db.get(models.Book, book_id)

def create_book(db: Session, *, title: str, description, price: float, url, category_id: int):
    obj = models.Book(
        title=title,
        description=description,
        price=price,
        url=url,
        category_id=category_id
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def update_book(db: Session, book_id: int, **fields):
    obj = get_book(db, book_id)
    if not obj:
        return None
    for k, v in fields.items():
        if v is not None:
            setattr(obj, k, v)
    db.commit()
    db.refresh(obj)
    return obj

def delete_book(db: Session, book_id: int):
    obj = get_book(db, book_id)
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True
