# Student Management System

## Описание проекта

Этот проект является веб-приложением для управления базой данных студентов. Включает следующие компоненты:
1. **API**: Разработан на Python с использованием FastAPI, взаимодействует с базой данных PostgreSQL.
2. **Frontend**: Разработан на React, отображает список студентов с поддержкой пагинации.
3. **База данных**: PostgreSQL, где хранятся данные студентов.

## Технологии

- **Backend**: FastAPI, SQLAlchemy, Pydantic
- **Frontend**: React, JavaScript
- **Database**: PostgreSQL
- **Containerization**: Docker, Docker Compose

## Установка

Для установки и запуска проекта выполните следующие шаги:

### 1. Клонируйте репозиторий

```sh
git clone https://github.com/vicoder98/lab2web.git
cd lab2web-main
```

### 2. Загрузите данные базы данных

```sh
docker volume create pgdata
docker run --rm -v pgdata:/var/lib/postgresql/data -v ${PWD}:/backup ubuntu tar xvf /backup/pgdata.tar -C /
```

### 3. Запустите проект

Чтобы запустить проект, используйте Docker Compose:

```sh
docker-compose up --build
```

Это команда создаст и запустит все необходимые контейнеры: API, frontend, и PostgreSQL.

### 4. Доступ к приложению

- Frontend будет доступен по адресу: `http://localhost:80`
- API будет доступен по адресу: `http://localhost:3000`

## API эндпоинты

1. **GET /students/** - Получить список студентов с поддержкой пагинации.
   - Параметры: `page`, `page_size`
2. **POST /students/** - Создать нового студента.
3. **DELETE /students/{id}** - Удалить студента по ID.
4. **PATCH /students/{id}** - Обновить данные студента по ID.
5. **GET /students/search/** - Поиск студентов по имени и фамилии.

## Пример запроса к API

Пример запроса для получения студентов с первой страницы, по 10 студентов на странице:

```sh
GET http://localhost:3000/students/?page=1&page_size=10
```


## Структура проекта

- **/api**: Python FastAPI backend
- **/frontend**: React frontend
- **/db**: PostgreSQL база данных
- **docker-compose.yml**: Файл для запуска всех микросервисов через Docker

## Дополнительные возможности

Проект поддерживает следующие дополнительные возможности:
- **CRUD операции**: создание, обновление, удаление записей студентов.
- **Пагинация**: возможность переключения страниц на frontend и backend.
- **Docker**: использование Docker для контейнеризации микросервисов.
- **Поиск и фильтрация**: возможность поиска студентов по имени и фамилии.

## Автор

Нгуен Тхе Вьет - N3347
