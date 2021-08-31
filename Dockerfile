FROM python:3.9.0

WORKDIR /home/

RUN echo "testing1234"

RUN git clone https://github.com/Jaegoomon/django_pinterest.git

WORKDIR /home/django_pinterest/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=pinterest.settings.deploy &&\
    python manage.py migrate --settings=pinterest.settings.deploy &&\
    gunicorn --env DJANGO_SETTINGS_MODULE=pinterest.settings.deploy pinterest.wsgi --bind 0.0.0.0:8000"]