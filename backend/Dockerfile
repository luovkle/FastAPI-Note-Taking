FROM python:3.9

WORKDIR /note-taking

COPY ./app/requirements.txt /note-taking

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app/alembic.ini /note-taking
COPY ./app/alembic /note-taking/alembic
COPY ./app/app /note-taking/app

run mkdir /note-taking/static

CMD [ \
    "gunicorn", "app.main:app", "--worker-class", \
    "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000" \
]
