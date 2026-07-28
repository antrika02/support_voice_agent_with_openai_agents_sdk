FROM python:3.12-slim

# Python settings
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Install build tools (needed by some Python packages)
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# FastAPI port
EXPOSE 8000

# Start FastAPI
CMD uvicorn app.main:app --host 0.0.0.0 --port 8000