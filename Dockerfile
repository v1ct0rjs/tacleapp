FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
  curl \
  build-essential \
  unzip \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

RUN bash remote_build.sh

EXPOSE 3000

# Comando simple - configuración en rxconfig.py
CMD ["reflex", "run"]