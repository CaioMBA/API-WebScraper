# Use an official Python runtime as a parent image
FROM python:3.13-slim

RUN apt-get update \
	&& apt-get install -y curl jq \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

ENV DEPLOYMENT_TARGET=Docker
ENV TZ=UTC
ENV HEALTHCHECK_BASEURL=http://localhost:80
ENV HEALTHCHECK_PATH=/Health

# Set the working directory in the container
WORKDIR /App

# Copy the current directory contents into the container at /app
COPY run.sh /App/
#COPY requirements.txt /app/

# Make the entrypoint script executable
RUN chmod +x /App/run.sh

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
 CMD sh -c 'curl -fs http://localhost:80/Health | jq -r ".status" | grep -qi "^Healthy$"'

# Run the entrypoint script
ENTRYPOINT ["/App/run.sh"]
