# Use official Python image
FROM python:3.13-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /core

# Install dependencies

RUN apt-get update && apt-get install -y \
	gcc \
	default-libmysqlclient-dev \
	pkg-config \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . .

# Collect static files (optional, for production)
# RUN python manage.py collectstatic --noinput

# Expose port (optional, depending on WSGI/ASGI server used)
EXPOSE 8000

# Command (can be overridden in docker-compose)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

