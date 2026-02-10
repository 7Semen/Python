## Запуск (Hello)
python3 app/hello.py

## Запуск (PostgreSQL)

### 1. Активируем виртуальное окружение
source venv/bin/activate

### 2. Убеждаемся, что PostgreSQL запущен
sudo service postgresql start

### 3. Инициализация базы
python3 -m app.init_db

### 4. Основной запуск приложения
python3 app/main.py

## Запуск (Работа с API)

### 1. Активируем виртуальное окружение
source venv/bin/activate

### 2. Установка зависимостей
pip install -r requirements.txt

### 3. Убеждаемся, что PostgreSQL запущен
sudo service postgresql start

### 4. Инициализация базы
python3 -m app.init_db

### 5. Основной запуск приложения
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

Swagger UI:
http://localhost:8000/docs

Health endpoint:
http://localhost:8000/health

Если localhost не открывается — используйте IP WSL.

Узнать IP можно командой:

hostname -I

После этого открыть:

http://<IP>:8000/docs
