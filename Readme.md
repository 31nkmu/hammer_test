Для установки потребуются следующие инструменты:
| Инструмент | Описание |
|----------|---------|
| [Python](https://www.python.org/downloads/) |  Язык программирования |
| [Poetry](https://python-poetry.org/) |  Менеджер зависимостей 

* Склонируй репозиторий используя команду
```Bash
# клонировать через HTTPS:
$ git clone https://github.com/31nkmu/hammer_test.git
# или клонировать через SSH:
$ git clone git@github.com:31nkmu/hammer_test.git
$ cd hammer_test
```
* Создай виртуальное окружение используя команду
```sh
$ poetry config virtualenvs.in-project true
$ poetry env use <your_python_version>
```

* Активируй виртуальное окружение
```sh
$ source .venv/bin/activate 
```

* Установи зависимости
```sh
$ poetry install
```
* Проведи миграции
```sh
$ make migrate
# создай суперпользователя
$ make createsuperuser-dev
```


## Запуск через docker-compose
Тебе понадобятся следующие инструменты
| Инструмент | Описание |
|----------|---------|
| [Docker](https://docs.docker.com/engine/install/ubuntu/) | Докер |
| [docker-compose](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04) | Докер-композ
Создай .env файл (смотри .env.example)
```sh
touch .env
```
Создай docker/.env файл (смотри docker/.env.example)
```sh
$ touch docker/.env
```

Запусти свой проект через docker-compose
```sh
make compose-collect-up
# создание суперпользователя в контейнере
make compose-createsuperuser
```
Смотри в Makefile для удобной работы с проектом


## Функциональность
#### Авторизация по номеру телефона:

* Отправьте `POST /api/v1/account/register/` с номером телефона. При успешном выполнении вы получите пароль авторизации.
  
```json
// Пример запроса
{
    "phone_number": "+996555802068"
}
// Пример ответа
{
    "phone_number": "+996555802068",
    "password": "2829",
    "invite_code": "0RHx18"
}
```

* Отправьте `POST /api/v1/account/login/` c номером телефона и паролем. При успешной аутентификации вы получите JWT-токен.

```json
// Пример запроса
{
    "phone_number": "+996555802068",
    "password": "2829",
}
// Пример ответа
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5MTYwODY4MywiaWF0IjoxNjkxNTIyMjgzLCJqdGkiOiIzYTFiODc1NDM1NzU0YzE3OGY5YzlmODhjZGEwNWVmNCIsInVzZXJfaWQiOjR9.jhZdrjcR38jvwd3fG3YJCMNHx3gXPq7LPwiXvLyS5LA",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkxOTU0MjgzLCJpYXQiOjE2OTE1MjIyODMsImp0aSI6IjJjYjY4NTk2ZTkxZTRlNDU5ZmEzZjM4ODAzNmUzOGU2IiwidXNlcl9pZCI6NH0.6eSJoRwCC8xdoCToze55SWnLbx6UsraiTjMqJj2lqqk"
}
```

#### Получение профиля:

* Отправьте `GET /api/v1/account/user/<user_id>/` для получения информации о своем профиле, включая активированный инвайт-код и список пользователей, которые ввели ваш инвайт-код.
```json
// Пример ответа
{
    "phone_number": "+996555802069",
    "invite_code": "PJdRkH",
    "invite_users": [
        {
            "phone_number": "+996555802068",
            "invite_code": "9gS5gb"
        },
        {
            "phone_number": "+996555802067",
            "invite_code": "0RHx18"
        }
    ]
}
```


#### Ввод чужого инвайт-кода:

* Отправьте `POST /api/v1/account/invite_code/` с введенным инвайт-кодом. Если инвайт-код существует, он будет связан с вашим профилем.
```json
// В заголовке добавьте токен 
"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkxOTU0MjgzLCJpYXQiOjE2OTE1MjIyODMsImp0aSI6IjJjYjY4NTk2ZTkxZTRlNDU5ZmEzZjM4ODAzNmUzOGU2IiwidXNlcl9pZCI6NH0.6eSJoRwCC8xdoCToze55SWnLbx6UsraiTjMqJj2lqqk"
// Пример запроса
{
    "invite_code": "PJdRkH"
}
// Пример ответа
{
    "invite_code": "0RHx18"
}
```


#### Получение всех пользователей:

* Отправьте `GET /api/v1/account/auth/` для получения информации обо всех пользователях.
```json
// Пример ответа
[
    {
        "phone_number": "+996555000000",
        "invite_code": "000000",
        "invite_users": []
    },
    {
        "phone_number": "+996555802068",
        "invite_code": "9gS5gb",
        "invite_users": [
            {
                "phone_number": "+996555802069",
                "invite_code": "PJdRkH"
            }
        ]
    },
    {
        "phone_number": "+996555802069",
        "invite_code": "PJdRkH",
        "invite_users": [
            {
                "phone_number": "+996555802068",
                "invite_code": "9gS5gb"
            },
            {
                "phone_number": "+996555802067",
                "invite_code": "0RHx18"
            }
        ]
    },
    {
        "phone_number": "+996555802067",
        "invite_code": "0RHx18",
        "invite_users": []
    }
]
```

