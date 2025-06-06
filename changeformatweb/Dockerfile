# --- STEP 1: Pakai base image Python slim
FROM python:3.10-slim

# --- STEP 2: Install dependensi sistem (termasuk LibreOffice)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      libreoffice-core \
      libreoffice-writer \
      libreoffice-calc \
      libreoffice-common && \
    rm -rf /var/lib/apt/lists/*

# --- STEP 3: Set working directory
WORKDIR /app

# --- STEP 4: Copy requirements dan install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- STEP 5: Copy semua source code
COPY . .

# --- STEP 6: Buat folder uploads dan converted
RUN mkdir -p /app/uploads /app/converted

# --- STEP 7: Expose port dan jalankan aplikasi dengan gunicorn
ENV PORT=5000
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
