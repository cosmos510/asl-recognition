# Use the Debian Slim image as the base
FROM debian:stable-slim

# Set environment variable for non-interactive mode
ENV DEBIAN_FRONTEND=noninteractive

# Install Nginx
RUN apt-get update && \
    apt-get install -y nginx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy your Nginx configuration file
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf

# Expose the port Nginx will listen on
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]