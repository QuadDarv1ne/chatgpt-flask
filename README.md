# Проект: ChatGPT Flask — Чат с ИИ



Это веб-приложение, которое предоставляет платформу для общения с искусственным интеллектом на основе ChatGPT.

Пользователи могут зарегистрироваться, войти в систему и вести разговор с ИИ в реальном времени.

## Технологии

- **Flask** — веб-фреймворк для Python, используемый для создания серверной части приложения.
- **Bootstrap** — фреймворк для стилизации интерфейса с возможностью быстрого и удобного создания адаптивных страниц.
- **SQLite** — легковесная база данных для хранения данных о пользователях и их сессиях.
- **Flask-Login** — расширение для управления сессиями и аутентификацией пользователей.
- **Flask-WTF** — расширение для работы с формами в Flask.
- **Flask-SQLAlchemy** — ORM для работы с базой данных SQLite.
- **OpenAI API** — для взаимодействия с искусственным интеллектом ChatGPT.

## Структура проекта

```
chatgpt-flask/
│
├── app/
│   ├── __init__.py          # Инициализация приложения
│   ├── config.py            # Конфигурация приложения (например, ключ API, настройки)
│   ├── routes/              # Папка для маршрутов
│   │   ├── __init__.py      # Инициализация маршрутов
│   │   ├── chat.py          # Маршруты для чатов
│   │   └── auth.py          # Маршруты для авторизации и регистрации
│   ├── templates/           # Шаблоны HTML
│   │   ├── base.html        # Основной шаблон
│   │   ├── index.html       # Главная страница
│   │   ├── login.html       # Страница авторизации
│   │   ├── register.html    # Страница регистрации
│   │   └── profile.html     # Профиль пользователя
│   ├── static/              # Статические файлы (CSS, JS, изображения)
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   └── models/              # Модели базы данных
│       ├── __init__.py      # Инициализация модели
│       └── user.py          # Модель пользователя для базы данных
├── migrations/              # Папка для миграций базы данных
├── .env                     # Переменные окружения (например, API-ключ)
├── requirements.txt         # Зависимости проекта
├── run.py                   # Точка входа для запуска приложения
└── venv/                    # Виртуальное окружение
```

## Миграции базы данных

**Чтобы использовать миграции для управления базой данных, выполните следующие команды:**

```bash
flask db init
flask db migrate
flask db upgrade
```

**Автор:** Дуплей Максим Игоревич

**Дата:** 10.12.2024
