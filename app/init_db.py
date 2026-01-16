from app.db.db import engine, get_session
from app.db.models import Base
from app.db import crud

def main():
    # 1) Создаём таблицы
    Base.metadata.create_all(bind=engine)

    db = get_session()
    try:
        # 2) Добавляем 2 категории (если ещё нет)
        cat1 = crud.get_category_by_title(db, "Фантастика") or crud.create_category(db, "Фантастика")
        cat2 = crud.get_category_by_title(db, "Программирование") or crud.create_category(db, "Программирование")

        # 3) В каждую категорию 2–4 книги (добавим, если пока книг нет)
        if len(crud.list_books_by_category(db, cat1.id)) == 0:
            crud.create_book(db, "Дюна", "Эпическая фантастика", 799, cat1.id, url=None)
            crud.create_book(db, "Нейромант", "Киберпанк-классика", 499, cat1.id, url=None)

        if len(crud.list_books_by_category(db, cat2.id)) == 0:
            crud.create_book(db, "Изучаем Python", "База по Python", 1200, cat2.id, url=None)
            crud.create_book(db, "Чистый код", "Практики качества кода", 950, cat2.id, url=None)

        print("База инициализирована: категории и книги добавлены.")
    finally:
        db.close()

if __name__ == "__main__":
    main()
