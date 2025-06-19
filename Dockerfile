FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app


RUN apt-get update && apt-get install -y \
  curl \
  build-essential \
  unzip \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .





ENV FRONTEND_PORT=${PORT:-3000}



ENV BACKEND_PORT=8000


EXPOSE ${FRONTEND_PORT}

CMD ["reflex", "run", "--env", "prod", "--frontend-port", "${FRONTEND_PORT}", "--backend-port", "${BACKEND_PORT}"]