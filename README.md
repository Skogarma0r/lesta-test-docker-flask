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


- **1‑2.**  [Создание и настройка репозитория][1-2]
- **3‑4.**  [Структура проекта, заполнение каталогов файлами][3-4]
- **5.**    [Настройка `.gitignore`, исключаем каталог от отслеживания][5]
- **6‑8.**  [Создание рабочих веток `feature/api` и `feature/ui`][6-8]
- **9‑11.** [Слияние ветки `feature/api` в `master` c `--no-ff`][9-11]
- **12‑14.**[Ребейз ветки `feature/ui` относительно `master`][12-14]
- **15‑16.**[Тег релиза `v1.0.0` с сообщением на объединённом коммите][15-16]
- **17‑18.**[Имитация и откат ошибочного коммита][17-18]
- **19‑21.**[Временные изменения (`git stash`)][19-21]
- **22‑23.**[Публикация на GitHub (SSH)][22-23]

[1-2]:   https://docs.google.com/document/d/e/2PACX-1vR--dEZtGafRIaOKawVLlo78XWSR_988vmo6t0-KZC67w4DtK8JKKGuFhPsXf443Za_-b8k9rT3usGd/pub#h.c3gwoka18nz5
[3-4]:   https://docs.google.com/document/d/e/2PACX-1vR--dEZtGafRIaOKawVLlo78XWSR_988vmo6t0-KZC67w4DtK8JKKGuFhPsXf443Za_-b8k9rT3usGd/pub#h.vq8s70tud401
[5]:     https://docs.google.com/document/d/e/2PACX-1vR--dEZtGafRIaOKawVLlo78XWSR_988vmo6t0-KZC67w4DtK8JKKGuFhPsXf443Za_-b8k9rT3usGd/pub#h.zsjxgd1ks02
[6-8]:   https://docs.google.com/document/d/e/2PACX-1vR--dEZtGafRIaOKawVLlo78XWSR_988vmo6t0-KZC67w4DtK8JKKGuFhPsXf443Za_-b8k9rT3usGd/pub#h.zehlsb1smaqg
[9-11]:  https://docs.google.com/document/d/e/2PACX-1vR--dEZtGafRIaOKawVLlo78XWSR_988vmo6t0-KZC67w4DtK8JKKGuFhPsXf443Za_-b8k9rT3usGd/pub#h.xto2widivnmw
[12-14]: https://docs.google.com/document/d/e/2PACX-1vR--dEZtGafRIaOKawVLlo78XWSR_988vmo6t0-KZC67w4DtK8JKKGuFhPsXf443Za_-b8k9rT3usGd/pub#h.tpjzmsqfh5vb
[15-16]: https://docs.google.com/document/d/e/2PACX-1vR--dEZtGafRIaOKawVLlo78XWSR_988vmo6t0-KZC67w4DtK8JKKGuFhPsXf443Za_-b8k9rT3usGd/pub#h.kkuwk1obl861
[17-18]: https://docs.google.com/document/d/e/2PACX-1vR--dEZtGafRIaOKawVLlo78XWSR_988vmo6t0-KZC67w4DtK8JKKGuFhPsXf443Za_-b8k9rT3usGd/pub#h.smaeuquk05ha
[19-21]: https://docs.google.com/document/d/e/2PACX-1vR--dEZtGafRIaOKawVLlo78XWSR_988vmo6t0-KZC67w4DtK8JKKGuFhPsXf443Za_-b8k9rT3usGd/pub#h.80wplu5p78xn
[22-23]: https://docs.google.com/document/d/e/2PACX-1vR--dEZtGafRIaOKawVLlo78XWSR_988vmo6t0-KZC67w4DtK8JKKGuFhPsXf443Za_-b8k9rT3usGd/pub#h.3bmgxs2vse24
