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

