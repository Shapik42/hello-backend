# Hello Backend

Базовый шаблон Python-проекта для отработки инструментов разработки.

## Требования
- Python 3.12+

## Установка и запуск

1. Клонируйте репозиторий и перейдите в папку проекта:
   ```bash
   git clone https://github.com/Shapik42/hello-backend.git
   cd hello-backend
   ```

2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Linux/macOS:
   source .venv/bin/activate
   ```

3. Установите инструменты разработки:
   ```bash
   pip install ruff pytest
   ```

4. Запустите приложение:
   ```bash
   python main.py
   ```

## Проверка кода и тесты

- Проверка линтером: `ruff check .`
- Форматирование кода: `ruff format .`
- Запуск тестов: `pytest`