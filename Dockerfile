FROM python:3.10-slim

# Install system dependencies (termasuk libreoffice dan deps-nya)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libreoffice \
    fonts-dejavu \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all app files
COPY . .

# Buat folder runtime
RUN mkdir -p /app/uploads /app/converted

# Expose port (optional, Railway auto-detect juga)
EXPOSE 5000

# Start pakai gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
