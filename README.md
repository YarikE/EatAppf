# EatApp - приложение для заказа еды

# Архитектура проекта
    Проект состоит из 2х приложений 
    1) Backend (папка EatApp)
    2) Frontend (папка eat_app_front)

    Для запуска проекта нужно запустить и Backend и Frontend приложения в разных консолях


# Запуск проекта


## Запускаем первую консоль и переходим в папку project 

## Запускаем виртуальное окружение и переходим в папку с backend приложением
    source venv/bin/activate
    cd EatApp

## Устанавливаем все зависимости backend приложения
    pip install -r requirements.txt

## Запускаем Backend приложение
    python3 manage.py runserver


## Запускаем вторую консоль и переходим в папку eat_app_front

## Устанавливаем все зависимости frontend приложения
    npm i

## Запускаем frontend приложение 
    npm run serve