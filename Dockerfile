# Use an appropriate base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install necessary system packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gettext \
    supervisor \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . /app

# Expose the port that the web server will use
EXPOSE 8000

# Command to start supervisord
CMD ["supervisord", "-c", "/app/supervisord.conf"]
