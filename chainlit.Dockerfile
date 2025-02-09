FROM --platform=linux/amd64 python:3.12.1-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

WORKDIR /app/src

EXPOSE 3500

CMD ["uvicorn", "--host=0.0.0.0", "main:app", "--port", "3500"]
