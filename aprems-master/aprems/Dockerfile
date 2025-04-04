### Dockerfile for Python Full Stack Django Application
##
### Use an official Python runtime as a parent image
##FROM python:3.12-slim
##
### Set environment variables
###ENV PYTHONDONTWRITEBYTECODE 1
###ENV PYTHONUNBUFFERED 1
##
### Set the working directory in the container
##WORKDIR /aprems
##
##
### Copy the requirements file and install dependencies
##COPY requirements.txt ./
##RUN pip install --no-cache-dir -r requirements.txt
##
##
##
### Copy the Django application into the container
##COPY . .
##
### Expose the port that Django runs on
##EXPOSE 8000
##
### Command to run the application
##CMD ["gunicorn", "aprems.wsgi:application", "--bind", "0.0.0.0:8000"]
#
#
#
## Use an official Python runtime as a parent image
#FROM python:3.11.4
#
## Set the working directory inside the container
#WORKDIR /aprems
#
## Copy only the requirements file to install dependencies first (for better caching)
#COPY requirements.txt ./
#
## Install dependencies
#RUN pip install --no-cache-dir -r requirements.txt
#
## Copy the entire Django project into the container
#COPY . .
#
## Collect static files (without user input)
#RUN python manage.py collectstatic --noinput
#
## Expose the port that the app runs on (inside the container)
#EXPOSE 8000
#
## Start the Gunicorn server
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "aprems.wsgi:application"]


# Use official Python image
FROM python:3.9

# Set working directory inside container
WORKDIR /aprems

# Copy project files into container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port (change if needed)
EXPOSE 8000

# Start Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
