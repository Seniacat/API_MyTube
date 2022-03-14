# API MyTube

### Описание
API для приложения MyTube - социальной сети для чтения и публикации постов и комментариев к ним.

## Технологии
- Python 3.7
- Django 3.2
- Django RESTFramework
- JWT + Joser

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Seniacat/api_final_yatube.git
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры

Список доступных эндпоинтов:

```
api/v1/posts/ - Получение публикаций
```
```
api/v1/posts/ - Список сообществ
```
```
api/v1/posts/{post_id}/comments/ - Комментарии к публикации
```
```
api/v1/follow/ - Подписки пользователя (доступен только аутентифицированным пользователям)
```
```
api/v1/jwt/create/ - Получение JWT-токена
```
```
api/v1/jwt/refresh/ - Обновление JWT-токена
```
```
api/v1/jwt/verify/ - Проверка JWT-токена
```
