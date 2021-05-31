# Урок 2. Шаблон + Контекст = html (Основы Django Frameworks)
Django GeekBrains Lessons 24.05.2021 

Задание 2. Шаблон + Контекст = html:
1. Организовать вывод динамического контента на страницах index и products (список товаров, заголовок страницы).
2. Поработать с шаблонными тегами и placeholder'ами (заглавные буквы, вывод текущей даты в шаблоне).
3. Реализовать в проекте механизмы работы c URL-адресами.
4. Реализовать наследование шаблонов в проекте.
5. Поработать со статическими файлами (убрать статическое объявление статики, переделав на динамическое отображение).

6*. Организовать загрузку динамического контента в контроллер products из json файла (добавив json файл в папку products/fixtures).

Реализованно:
1. Вывод трех товаров(products) из словаря context с помощью конструкции:

 {% if products %}
    {% for product in products %}
        <h3> {{ product.name }}</h3>
        <p> {{ product.price }}</p>
        <p> {{ product.about }}</p>
    {% endfor %}
{% else %}
    <h2>Товаров на складе нет!</h2>
{% endif %}

2. Использованные Placeholder'ы:

  index.html  
    {% now "d.m.y H:i" %}
  products.html
    {% now "Y" %}
    {% now "jS F Y H:i" %}
    
6. В процессе...
    
