Простой сервис для сокращения URL. Сохраняет короткое представление введенного URL (hash blake2b), и перенаправляет на исходный URL.
Также считает количество переходов по короткой ссылке.
Flask, SQLAlchemy (DB - Postgres)

1. Install packages:
$ pip install -r requirements.txt
2. Change database parameters in config.yaml
3. Run app:
$ python runserver.py
