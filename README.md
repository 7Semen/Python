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

