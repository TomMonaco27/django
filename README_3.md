Урок 3. Модели + ORM = данные

1. Создать модели в проекте (обязательно должно быть поле с изображениями) и выполнить миграции.
2. Поработать с моделями в консоли.
3. Создать суперпользователя. Настроить админку и поработать в ней.
4. Организовать работу с моделями в контроллерах и шаблонах.
5. Настроить проект для работы с медиафайлами (добавить media в .gitignore).
6*. Создать диспетчер URL в приложении. Скорректировать динамические URL-адреса в шаблонах.
7*. Организовать загрузку данных в базу из файла (Django fixtures).

 

Решения:

Запуск миграций и сервера:

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

Создание суперпользователя:

python manage.py createsuperuser

 
загрузки в/из баз данных из файла:

python manage.py dumpdata products.ProductCategory > categories.json

python manage.py dumpdata products.Product > product.json

python manage.py loaddata products/fixtures/categories.json

python manage.py loaddata products/fixtures/product.json
