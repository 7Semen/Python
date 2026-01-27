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

### 2. Убеждаемся, что PostgreSQL запущен
sudo service postgresql start

### 3. Инициализация базы
python3 -m app.init_db

### 4. Основной запуск приложения
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/health
