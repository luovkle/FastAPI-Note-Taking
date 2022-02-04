# FastAPI Note Taking

## Requirements

* python3.9
* pipenv
* postgresql
* docker (optional)

### Notes:

**FastAPI Note Taking** requires a connection to a postgres database with the following data postgresql://user:password@127.0.0.1/app

Running a postgres container with docker

```sh
docker run --name postgres --rm -d -p 5432:5432 -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -e POSTGRES_DB=app postgres:13.3-alpine
```

## Usage

```sh
git clone https://github.com/luovkle/FastAPI-Note-Taking
cd FastAPI-Note-Taking/backend/app
pipenv install
pipenv shell
alembic upgrade head
uvicorn --reload app.main:app
```
