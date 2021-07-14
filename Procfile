release: python3 manage.py migrate
web: daphne simplecapp_api.asgi:application --port $PORT --bind 0.0.0.0 -v2   