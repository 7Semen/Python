from sqlalchemy import select
from sqlalchemy.orm import Session
from .models import Category, Book

# ---------- Categories CRUD ----------

def create_category(db: Session, title: str) -> Category:
    cat = Category(title=title)
    db.add(cat)
    db.commit()
    db.refresh(cat)
    return cat

def get_category_by_id(db: Session, category_id: int) -> Category | None:
    return db.get(Category, category_id)

def get_category_by_title(db: Session, title: str) -> Category | None:
    return db.execute(select(Category).where(Category.title == title)).scalar_one_or_none()

def list_categories(db: Session) -> list[Category]:
    return list(db.execute(select(Category).order_by(Category.id)).scalars().all())

def update_category(db: Session, category_id: int, new_title: str) -> Category | None:
    cat = db.get(Category, category_id)
    if not cat:
        return None
    cat.title = new_title
    db.commit()
    db.refresh(cat)
    return cat

def delete_category(db: Session, category_id: int) -> bool:
    cat = db.get(Category, category_id)
    if not cat:
        return False
    db.delete(cat)
    db.commit()
    return True

# ---------- Books CRUD ----------

def create_book(
    db: Session,
    title: str,
    description: str,
    price: int,
    category_id: int,
    url: str | None = None,
) -> Book:
    book = Book(title=title, description=description, price=price, category_id=category_id, url=url)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def get_book_by_id(db: Session, book_id: int) -> Book | None:
    return db.get(Book, book_id)

def list_books(db: Session) -> list[Book]:
    return list(db.execute(select(Book).order_by(Book.id)).scalars().all())

def list_books_by_category(db: Session, category_id: int) -> list[Book]:
    return list(db.execute(select(Book).where(Book.category_id == category_id).order_by(Book.id)).scalars().all())

def update_book_price(db: Session, book_id: int, new_price: int) -> Book | None:
    book = db.get(Book, book_id)
    if not book:
        return None
    book.price = new_price
    db.commit()
    db.refresh(book)
    return book

def delete_book(db: Session, book_id: int) -> bool:
    book = db.get(Book, book_id)
    if not book:
        return False
    db.delete(book)
    db.commit()
    return True
