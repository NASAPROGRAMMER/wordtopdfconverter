FROM python:3.10-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    libreoffice fonts-dejavu && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /app/uploads /app/converted

EXPOSE 5000

# FIXED: Gunakan shell command agar $PORT bisa terbaca
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:$PORT app:app"]
