FROM python:3.7

EXPOSE 8000
WORKDIR /app

RUN pip install pipenv
COPY Pipfile* ./
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt
COPY . .

CMD gunicorn main:app -b 0.0.0.0:8000