# Flask + Redis Docker Project

Простой EndPoint с использованием Flask и счётчиком посещений на Redis.
Реализовано с использованием Docker и docker compose.

---

## Структура проекта
```
├── app/                  # Flask-приложение
│   └── app.py
├── docker/               # Dockerfile и docker-compose.yaml
│   ├── Dockerfile
│   └── docker-compose.yaml
├── requirements.txt      # Python-зависимости
├── ui/                   # Фронтенд (каталог создан в рамках HW2)
│   └── index.html
└── README.md             # Описание проекта и инструкции
```
## Запуск проекта

### 1. Перейти в каталог с Docker-файлами

```
cd docker/
```
### 2. Собрать контейнеры
```
docker compose build
```
### 3. Запустить контейнеры в фоновом режиме
```
docker compose up -d
```
### 4. Использовать curl-запросы в терминале или перейти по ссылке в браузере
```
curl http://localhost:5000/ping
# {"status": "ok"}

curl http://localhost:5000/count
# {"visits": 1}
```

## Действия с  контейнерами

### Остановка контейнеров
```
docker compose stop
```
### Остановка и удаление контейнеров
```
docker compose down
```
### Перезапуск контейнеров
```
docker compose restart
```

## Просмотр логов контейнеров
```
docker compose ps           # Список запущенных контейнеров
docker compose logs         # Просмотр логов всех контейнеров
docker compose logs web     # Просмотр логов отдельного контейнера
docker compose logs -f web  # Просмотр логов в реальном времени
```

# Практика Git (Flask + Docker API)

> **Проект:** `docker-flask-test`  
> **Цель:** отработать ветвление, слияния, откаты, `stash`, теги и публикацию в git
---

## Содержание
1-2.   [Создание и настройка репозитория]
3-4.   [Структура проекта, заполнение каталогов файлами]
5.     [Настройка .gitignore]
6-8.   [Рабочие ветки `feature/api` и `feature/ui`]
9-14.  [Слияние / ребейз / история]
15-16. [Тег `v1.0.0`]
17-18. [Имитация и откат ошибочного коммита]
19-21. [Временные изменения `git stash`]
22-23. [Публикация на GitHub (SSH)]
