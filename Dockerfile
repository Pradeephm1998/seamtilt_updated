# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files into container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set entrypoint to run the script
CMD ["python", "scripts/run_seamtilt.py"]
