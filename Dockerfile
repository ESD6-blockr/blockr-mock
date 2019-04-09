FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN apt-get update

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y nodejs
RUN apt-get clean -y

RUN mkdir /code
WORKDIR /code

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . /code

EXPOSE 8000

HEALTHCHECK CMD curl -f http://localhost:8000 || exit 1

CMD  python wait_for_postgres.py && ./manage.py migrate && gunicorn --chdir erp --bind 0.0.0.0:8000 erp.wsgi:application
