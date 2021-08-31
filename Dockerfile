FROM python:3.9.0

RUN mkdir /root/.ssh

# host to container
ADD ./.ssh/id_rsa /root/.ssh/id_rsa

RUN chmod 600 /root/.ssh/id_rsa

RUN touch /root/.ssh/known_hosts

RUN ssh-keyscan github.com >> /root/.ssh/know_hosts

WORKDIR /home/

RUN echo "testing1234"

RUN git clone git@github.com:Jaegoomon/django_project_private.git

WORKDIR /home/django_project_private/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=pinterest.settings.deploy &&\
    python manage.py migrate --settings=pinterest.settings.deploy &&\
    gunicorn --env DJANGO_SETTINGS_MODULE=pinterest.settings.deploy pinterest.wsgi --bind 0.0.0.0:8000"]