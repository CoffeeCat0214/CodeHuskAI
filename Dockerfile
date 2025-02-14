# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Install git and any required system dependencies
RUN apt-get update && \
    apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the refactoring_agent project files into the container
COPY . /app

# The agent is a CLI-based app that runs from main.py.
# Environment variable OPENAI_API_KEY will be provided at runtime.
CMD ["python", "main.py"] 