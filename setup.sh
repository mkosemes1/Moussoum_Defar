#!/bin/bash
# Quick setup script for Moussoum Defar

set -e

echo "========================================="
echo "  Moussoum Defar - African AI Platform"
echo "========================================="
echo ""

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "Error: Docker is not installed."
    echo "Please install Docker: https://docs.docker.com/get-docker/"
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "Error: Docker Compose is not installed."
    echo "Please install Docker Compose: https://docs.docker.com/compose/install/"
    exit 1
fi

# Copy environment file
if [ ! -f .env ]; then
    echo "Creating .env file from .env.example..."
    cp .env.example .env
    echo ".env file created."
else
    echo ".env file already exists."
fi

echo ""
echo "Starting Docker containers..."
docker-compose up -d

echo ""
echo "Waiting for services to start..."
sleep 10

echo ""
echo "Running migrations..."
docker-compose exec web python manage.py migrate

echo ""
echo "Loading African benchmarks..."
docker-compose exec web python manage.py load_benchmarks

echo ""
echo "========================================="
echo "  Setup Complete!"
echo "========================================="
echo ""
echo "Next steps:"
echo "1. Create a superuser: docker-compose exec web python manage.py createsuperuser"
echo "2. Access the admin: http://localhost:8000/admin/"
echo "3. Access API docs: http://localhost:8000/api/docs/"
echo ""
echo "To start the development server:"
echo "  docker-compose up"
echo ""
