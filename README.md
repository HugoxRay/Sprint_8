# Sprint_5
Автоматизированное тестирование учебного сервиса Stellar Burgers.
* Python
* Selenium
* Pytest
* Google Chrome

## Структура проекта
Sprint_5/
│
├── tests/
│   ├── test_constructor.py
│   ├── test_login.py
│   ├── test_navigation.py
│   └── test_registration.py
│
├── conftest.py
├── helpers.py
├── locators.py
├── requirements.txt
├── README.md
└── .gitignore

## Проверяемая функциональность

### Регистрация

* успешная регистрация;
* ошибка при вводе пароля менее шести символов.

### Вход

* вход через кнопку «Войти в аккаунт»;
* вход через кнопку «Личный кабинет»;
* вход через страницу регистрации;
* вход через страницу восстановления пароля.

### Личный кабинет

* переход в личный кабинет;
* переход в конструктор через кнопку «Конструктор»;
* переход в конструктор через логотип Stellar Burgers;
* выход из аккаунта.

### Конструктор

* переход к разделу «Булки»;
* переход к разделу «Соусы»;
* переход к разделу «Начинки».

## Установка зависимостей

pip install -r requirements.txt

## Запуск тестов

pytest -v

python -m pytest tests/test_registration.py -v
python -m pytest tests/test_login.py -v
python -m pytest tests/test_navigation.py -v
python -m pytest tests/test_constructor.py -v