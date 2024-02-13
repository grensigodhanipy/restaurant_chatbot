# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5005

# Define environment variable
ENV RASA_ENV=production

# Command to run the Rasa server when the container starts
CMD ["rasa", "run", "-m", "models", "--enable-api", "--cors", "*", "--debug"]
