ARG PYTHON_VERSION=3.12.1

FROM python:${PYTHON_VERSION}

RUN apt-get -y update
RUN apt-get -y upgrade

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir -p /code

WORKDIR /code

RUN pip install poetry
COPY pyproject.toml poetry.lock /code/
RUN poetry config virtualenvs.create false

RUN poetry install --only main --no-root --no-interaction
COPY . /code

EXPOSE 80

WORKDIR /code/form_builder

CMD ["/bin/bash", "-c", "python manage.py collectstatic --noinput; gunicorn --bind :8000 --workers=3 --threads=3 --timeout 60 --worker-class=gthread transparency.wsgi"]
