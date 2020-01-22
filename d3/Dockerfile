FROM python:3.7

WORKDIR /app

RUN pip install pipenv
COPY Pipfile* ./
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt
COPY . .

WORKDIR /app/itemer
CMD gunicorn -k uvicorn.workers.UvicornWorker itemer.asgi:application -b localhost:8080 --workers 80