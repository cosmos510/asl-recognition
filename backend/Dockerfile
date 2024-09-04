# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory
WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]