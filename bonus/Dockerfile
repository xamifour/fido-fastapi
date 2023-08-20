# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory within the container
WORKDIR /app

# Copy the requirements file into the container
COPY ./requirements.txt .

# Install project dependencies using pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app directory into the container
COPY ./fastapp /app

# Expose the port on which the FastAPI application will run
EXPOSE 8001

# Command to start the FastAPI application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
