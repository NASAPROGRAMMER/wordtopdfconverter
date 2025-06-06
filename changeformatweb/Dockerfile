# --- STEP 1: Pakai base image Python slim
FROM python:3.10-slim

# --- STEP 2: Install dependensi sistem (termasuk libreoffice)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      libreoffice-core \
      libreoffice-writer \
      libreoffice-calc \
      libreoffice-common && \
    rm -rf /var/lib/apt/lists/*

# --- STEP 3: Copy requirements dan install Python packages
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# --- STEP 4: Copy semua source code ke /app
COPY . /app

# --- STEP 5: Ekspos port yang akan digunakan Flask
ARG PORT=5000
ENV PORT=${PORT}

# --- STEP 6: Pastikan folder uploads/ dan converted/ ada
RUN mkdir -p /app/uploads /app/converted

# --- STEP 7: Jalankan Flask
#      (Flask nanti membaca env PORT; jika tidak ada, default 5000)
CMD ["gunicorn", "--bind", "0.0.0.0:${PORT}", "app:app"]
