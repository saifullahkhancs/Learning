# Build Python backend
FROM python:3.10-slim AS backend

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install system dependencies and python packages
COPY requirements.txt .
RUN apt-get update && \
    apt-get install -y netcat-traditional && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get purge -y --auto-remove && \
    rm -rf /var/lib/apt/lists/*

# Copy all source code
COPY . .

# Copy and set executable for entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Expose port and run the application
EXPOSE 8000
ENTRYPOINT ["/entrypoint.sh"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]