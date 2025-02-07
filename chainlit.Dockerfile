FROM --platform=linux/amd64 python:3.12.1-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["chainlit", "run", "src/app.py"]
