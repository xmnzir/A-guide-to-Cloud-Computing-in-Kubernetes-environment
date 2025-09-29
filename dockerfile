# Base image
FROM python:3.9-slim

# Install curl for connectivity checks
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy Python script
COPY LoadGenerator.py /app/LoadGenerator.py

# Install dependencies
RUN pip install requests

# Run script
ENTRYPOINT ["python3", "LoadGenerator.py"]
