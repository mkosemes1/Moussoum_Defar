# Moussoum Defar - African AI Platform

Data and AI intelligence infrastructure for Africa.

## Overview

This platform provides specialized infrastructure to understand, measure, and improve AI in African contexts. It consists of three main pillars:

### 1. African Data Hub
- Local data collection (text, voice, images)
- Paid African workers for data collection
- Quality and validation system
- Ready-to-use datasets for AI companies

### 2. AI Evaluation Lab
- AI model testing against African benchmarks
- Contextual understanding evaluation
- Detailed reports by country and category
- API for automated integration

### 3. AI Workforce
- Network of African workers (students, linguists, experts)
- Leveling and reputation system
- Payment via Mobile Money
- Skills economy around AI

## Technical Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    FRONTEND (Django Templates)          │
│  ┌──────────────────┐  ┌──────────────────┐            │
│  │  Worker Portal    │  │  Client Portal    │           │
│  └──────────────────┘  └──────────────────┘            │
└───────────────────────┬─────────────────────────────────┘
                        │
┌───────────────────────┴─────────────────────────────────┐
│                   DJANGO BACKEND (API + Logic)           │
│  ┌─────────────┐ ┌──────────────┐ ┌────────────────┐  │
│  │ Data Hub    │ │ Evaluation   │ │ Worker Scoring │  │
│  │ Module      │ │ Lab Module   │ │ Module         │  │
│  └─────────────┘ └──────────────┘ └────────────────┘  │
└───────────┬───────────────┬───────────────┬─────────────┘
            │               │               │
    ┌───────┴──┐    ┌──────┴───┐    ┌──────┴──────┐
    │PostgreSQL│    │  Redis   │    │   MinIO     │
    └──────────┘    └──────────┘    └─────────────┘
```

## Tech Stack

| Component | Choice | Cost/month |
|---|---|---|
| Backend | Django 5 + Django REST Framework | $0 |
| Database | PostgreSQL 16 | ~$25 |
| Cache + Queue | Redis | ~$15 |
| File Storage | MinIO (self-hosted) | $0 |
| Async Tasks | Celery + Redis | $0 |
| Server | Hetzner CX32 | ~$10 |
| SSL + Proxy | Caddy | $0 |
| **Total** | | **~$50/month** |

## Installation

### Prerequisites

- Docker and Docker Compose installed
- Python 3.11+ (for local development)
- Git

### Setup with Docker (Recommended)

```bash
# Clone the repository
git clone <repository-url>
cd Moussoum_Defar

# Copy the environment file
cp .env.example .env

# Start the services
docker-compose up -d

# Create the database and tables
docker-compose exec web python manage.py migrate

# Create a superuser
docker-compose exec web python manage.py createsuperuser

# Start the development server
docker-compose up
```

### Local Setup (Without Docker)

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure the database
# Edit settings in Moussoum_Defar/settings.py

# Run migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Start the server
python manage.py runserver
```

## Project Structure

```
Moussoum_Defar/
├── Moussoum_Defar/           # Django Configuration
│   ├── settings.py           # Main settings
│   ├── urls.py               # Root URLs
│   ├── wsgi.py               # WSGI
│   └── asgi.py               # ASGI
├── workers/                  # Data Hub + Workforce Module
│   ├── models.py             # Worker, Collection, etc. models
│   ├── serializers.py        # API serializers
│   ├── views.py              # API views
│   ├── urls.py               # API routes
│   ├── admin.py              # Admin interface
│   └── scoring.py            # Scoring system
├── evaluation/               # AI Evaluation Lab Module
│   ├── models.py             # Benchmark, Evaluation, etc. models
│   ├── serializers.py        # API serializers
│   ├── views.py              # API views
│   ├── urls.py               # API routes
│   ├── admin.py              # Admin interface
│   ├── scoring.py            # AI scoring system
│   └── benchmarks/           # African benchmarks
│       ├── senegal.py        # Senegal benchmark
│       ├── nigeria.py        # Nigeria benchmark
│       └── kenya.py          # Kenya benchmark
├── clients/                  # Client Module
│   ├── models.py             # Client, Subscription models
│   ├── serializers.py        # API serializers
│   ├── views.py              # API views
│   ├── urls.py               # API routes
│   └── admin.py              # Admin interface
├── templates/                # HTML templates
├── static/                   # Static files
├── docker-compose.yml        # Docker orchestration
├── Dockerfile                # Docker image
├── requirements.txt          # Python dependencies
└── .env.example              # Environment variables
```

## API Endpoints

### Authentication

```
POST   /api/v1/auth/register/           → Register
POST   /api/v1/auth/login/              → Login
POST   /api/v1/auth/refresh/            → Refresh token
```

### Workers (Data Hub)

```
GET    /api/v1/workers/me/              → Worker profile
PUT    /api/v1/workers/me/              → Update profile
GET    /api/v1/workers/me/score/        → Quality score
GET    /api/v1/workers/me/tasks/        → Assigned tasks
GET    /api/v1/workers/me/earnings/     → Earnings
GET    /api/v1/collections/             → Available projects
POST   /api/v1/collections/{id}/submit/ → Submit data
```

### Evaluation Lab

```
GET    /api/v1/benchmarks/              → List benchmarks
GET    /api/v1/benchmarks/{id}/         → Benchmark details
GET    /api/v1/benchmarks/{id}/tests/   → Test cases
POST   /api/v1/evaluations/             → Create evaluation
GET    /api/v1/evaluations/{id}/        → Results
GET    /api/v1/evaluations/{id}/report/ → Detailed report
POST   /api/v1/models/test/             → Quick model test
```

### Clients

```
GET    /api/v1/clients/me/              → Client profile
GET    /api/v1/clients/me/usage/        → Usage
POST   /api/v1/clients/me/subscription/ → Manage subscription
```

## Development

### Running Tests

```bash
# All tests
docker-compose exec web python manage.py test

# Specific module tests
docker-compose exec web python manage.py test workers
docker-compose exec web python manage.py test evaluation
```

### Adding a New Benchmark

1. Create a file in `evaluation/benchmarks/`
2. Define test cases in JSON format
3. Load the benchmark into the database:
```bash
docker-compose exec web python manage.py load_benchmarks
```

### Developing a New Endpoint

1. Add the model in `models.py`
2. Create the serializer in `serializers.py`
3. Add the view in `views.py`
4. Register the route in `urls.py`

## Data Model

### Workers

- **Worker**: African worker profile
- **Language**: Supported languages
- **Country**: African countries
- **WorkerLevel**: Level and progression requirements
- **QualityLog**: Quality history

### Data Hub

- **DataCollection**: Collection project
- **DataSubmission**: Worker data submission

### Evaluation

- **AfricanBenchmark**: Benchmark by country/context
- **TestCase**: Individual test case
- **Evaluation**: Model evaluation
- **TestExecution**: Test execution result

### Clients

- **Client**: Company/startup profile
- **Subscription**: Subscription plan
- **APIKey**: API access key

## Security

- JWT authentication
- API rate limiting
- Input validation
- Sensitive data encryption
- GDPR compliance

## Deployment

### Production

```bash
# Build the image
docker-compose -f docker-compose.prod.yml build

# Deploy
docker-compose -f docker-compose.prod.yml up -d

# Apply migrations
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate

# Collect static files
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic
```

## License

Proprietary - All rights reserved.

## Contact

For any questions: contact@moussoumdefar.com
