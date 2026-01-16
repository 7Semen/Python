from app.db.db import get_session
from app.db import crud

def main():
    db = get_session()
    try:
        categories = crud.list_categories(db)
        print("Категории:")
        for c in categories:
            print(f"- [{c.id}] {c.title}")

        print("\nКниги:")
        books = crud.list_books(db)
        for b in books:
            print(f"- [{b.id}] {b.title} | {b.price} | category_id={b.category_id}")
    finally:
        db.close()

if __name__ == "__main__":
    main()
