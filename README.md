## Технологии:
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)

## Задача
###### Часть 1
Создать модели с полями. Вынести их в админ-панель.

Товар:
 - Название
 - Картинка
 - Контент
 - Стоимость

Заказ:
 - Итоговая сумма
 - Статус
 - Время создания
 - Время подтверждения

Платеж:
 - Сумма
 - Статус
 - Тип оплаты
###### Часть 2
Создать эндпоинты.

**Эндпоинт получения списка Товаров:**
- GET-запрос с выдачей списка Товаров.

**Эндпоинт создания нового Заказа:**
- POST-запрос с указанием списка Товаров. Итоговая сумма Заказа должна складываться из стоимостей всех Товаров. Во Время создания должен записываться текущий таймстамп.

**Эндпоинт создания нового Платежа:**
- POST-запрос с указанием Заказа. Сумма должна браться из итоговой суммы Заказа.
###### Часть 3
Добавить в админке к модели Заказ кнопку подтверждения заказа. Она должна отображаться только если связанный Платеж имеет статус “Оплачен”. При нажатии на кнопку нужно изменить статус Заказа на “Подтвержден”, сохранить текущую дату и время в поле Время подтверждения. Сымитировать подготовку заказа (можно просто через sleep на несколько секунд) и отправить POST-запрос по адресу https://webhook.site/36693e00-8f59-4f7b-9a85-1d1e7ddde4d4 с телом JSON {"id":ИД_ЗАКАЗА, "amount":СУММА_ЗАКАЗА,”date”:ВРЕМЯ_ПОДТВЕРЖДЕНИЯ}

## Запуск проекта
Создать файл окружения и заполнить необходимыми параметрами:
```
touch .env
SECRET_KEY='your_key'
DEBUG=0
DB_NAME= # имя базы данных
POSTGRES_USER= # логин для подключения к базе данных
POSTGRES_PASSWORD= # пароль для подключения к БД 
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
```
#### Запуск через docker
Клонируйте репозиторий, перейдите в папку, установите docker и docker-compose если нужно.
Запустить приложения в контейнерах:
```
docker-compose up --build
```
или для запуска в фоном режиме:
```
docker-compose up -d --build
```
### После успешной сборки выполните команды:
#### Выполните миграции:
```
docker-compose exec web python manage.py migrate
docker-compose exec backend python manage.py collectstatic --no-input
```
#### Создать суперпользователя Django:
```
docker-compose exec web python manage.py createsuperuser
```
#### Проект будет доступен по адрессу:
* http://localhost/
* http://localhost/backend/admin - админка
* http://localhost/backend/docs/ - swagger
#### Остановить контейнер:
```
docker-compose stop
```
### Автор
Selivanov Dmitry