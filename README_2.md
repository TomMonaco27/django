# Урок 2. Шаблон + Контекст = html (Основы Django Frameworks)
Django GeekBrains Lessons 24.05.2021 

Задание 2. Шаблон + Контекст = html:
1. Организовать вывод динамического контента на страницах index и products (список товаров, заголовок страницы).
2. Поработать с шаблонными тегами и placeholder'ами (заглавные буквы, вывод текущей даты в шаблоне).
3. Реализовать в проекте механизмы работы c URL-адресами.
4. Реализовать наследование шаблонов в проекте.
5. Поработать со статическими файлами (убрать статическое объявление статики, переделав на динамическое отображение).

6*. Организовать загрузку динамического контента в контроллер products из json файла (добавив json файл в папку products/fixtures).

# Урок 2. Реализованно:
1. Вывод трех товаров(products) из словаря context с помощью конструкции:

 {% if products %}
    {% for product in products %}
        <p> {{ product.name }}</p>
        <p> {{ product.price }}</p>
        <p> {{ product.about }}</p>
    {% endfor %}
{% else %}
    <p>Товаров на складе нет!</p>
{% endif %}

2. Использованные Placeholder'ы:

  index.html  
    {% now "d.m.y H:i" %}
  products.html
    {% now "Y" %}
    {% now "jS F Y H:i" %}
    
6. В процессе...

8. Иллюстрации:
![Иллюстрация к проекту](https://github.com/TomMonaco27/django/blob/lesson-2/Index2.png)
![Иллюстрация к проекту](https://github.com/TomMonaco27/django/blob/lesson-2/footer2.png)
![Иллюстрация к проекту](https://github.com/TomMonaco27/django/blob/lesson-2/Products2.png)

