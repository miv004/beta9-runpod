FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set up the working directory
WORKDIR /app

# Copy the application files
COPY . .

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose the port
EXPOSE 8080

# Start the server
CMD ["python", "handler.py"]