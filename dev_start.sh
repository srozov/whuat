fuser -k 8000/tcp
python3 manage.py makemigrations
python3 manage.py makemigrations mqm_app
python3 manage.py migrate
python3 manage.py collectstatic --clear --noinput
python3 manage.py runserver 0.0.0.0:8004