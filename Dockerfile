# Use an official lightweight Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the main Python script into the container
COPY umbrella.py .

# Set environment variables for Python to run correctly
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Command to run the script when the container starts
# The .env file will be passed in at runtime, not built into the image
CMD [ "python", "umbrella.py" ]
