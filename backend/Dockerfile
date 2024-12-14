# Base Image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy dependency file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Add non-root user for security
RUN useradd -ms /bin/bash appuser
USER appuser

# Copy application code
COPY . .

# Environment variables
ENV FLASK_APP=app.py \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_ENV=production \
    DB_HOST=db \
    DB_PORT=5432 \
    DB_USER=user \
    DB_PASSWORD=password \
    DB_NAME=court_rulings

# Run application with Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:create_app()"]
