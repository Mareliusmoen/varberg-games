web: gunicorn varberggames.wsgi
worker: daphne varberggames.asgi:application
worker: python manage.py runworker -v2