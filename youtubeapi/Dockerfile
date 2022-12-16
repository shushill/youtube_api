FROM python:3.8.9-alpine

RUN mkdir /app
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

RUN pip install --upgrade pip
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev libc-dev linux-headers

COPY ./requirements.txt .

COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# CMD ["/scripts/entrypoint.sh"]
