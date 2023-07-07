# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory to the container
COPY . .

# Set the environment variables
ENV SELENIUM_URL="http://localhost:4444"

# Set the entry point to the main.py file
CMD ["python", "-u", "main.py"]