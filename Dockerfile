# Use the official Python base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code to the container
COPY . /code/

# Expose the default Django development server port
EXPOSE 8000

# Run database migrations
RUN python manage.py migrate

RUN python -c "import os; from django.contrib.auth import get_user_model; User = get_user_model(); \
    User.objects.filter(username=os.getenv('DJANGO_SUPERUSER_USERNAME')).exists() or \
    User.objects.create_superuser(os.getenv('DJANGO_SUPERUSER_USERNAME'), \
    os.getenv('DJANGO_SUPERUSER_EMAIL'), os.getenv('DJANGO_SUPERUSER_PASSWORD'))" | python manage.py shell


# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
