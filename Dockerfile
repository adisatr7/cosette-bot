# Use the official Python image as the base image
FROM python:3-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install pre-release version of py-cord. Installing directly from
# requirements.txt doesn't work for some reason.
RUN pip install -U py-cord --pre

# Copy the rest of the source code to the container
COPY . .

# Set the entrypoint command to run the bot
CMD ["python", "App.py"]