# UI-тесты Stellar Burgers

Проект содержит UI-тесты основной функциональности и раздела «Лента заказов». Элементы и действия описаны с помощью Page Object. Все тесты запускаются в Google Chrome и Mozilla Firefox.

## Установка

На компьютере должны быть установлены Chrome и Firefox.

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Для Windows:

```bash
venv\Scripts\activate
```

## Запуск тестов и создание Allure-результатов

```bash
pytest --alluredir=allure_results --clean-alluredir
```

## Просмотр Allure-отчёта

```bash
allure serve allure_results
```

## Покрытые сценарии

- переход в «Конструктор»;
- переход в «Ленту заказов»;
- открытие и закрытие окна с деталями ингредиента;
- увеличение счётчика ингредиента после добавления в заказ;
- увеличение счётчиков заказов за всё время и за сегодня;
- появление номера нового заказа в разделе «В работе».
