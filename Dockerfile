# Use an official Python runtime as a parent image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY run.sh /app/
#COPY requirements.txt /app/

# Make the entrypoint script executable
RUN chmod +x /app/run.sh

# Run the entrypoint script
ENTRYPOINT ["/app/run.sh"]
