# Moussoum Defar

**Data and AI infrastructure for Africa**

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.0+-green.svg)](https://djangoproject.com)
[![License](https://img.shields.io/badge/License-Non--Commercial-blue.svg)](LICENSE)

---

## Why Moussoum Defar?

AI doesn't understand Africa. Models trained on Western data fail with:
- African languages (Wolof, Swahili, Hausa, Yoruba...)
- Local systems (Mobile Money, FCFA, NIN, KRA...)
- Cultural context (Teranga, Jollof Rice, Maasai traditions...)

**Moussoum Defar is the missing infrastructure to make AI reliable in Africa.**

---

## Features

### African Data Hub
- Collect text, voice, and image data from African communities
- Pay workers via Mobile Money
- Quality scoring and validation system

### AI Evaluation Lab
- Test AI models against African benchmarks
- 62 test cases across 3 countries (Senegal, Nigeria, Kenya)
- Detailed reports by category and language

### AI Workforce
- Network of African workers (students, linguists, experts)
- 5-level progression system
- Quality reputation scoring

---

## Quick Start

```bash
# Clone
git clone https://github.com/yourusername/Moussoum_Defar.git
cd Moussoum_Defar

# Setup
cp .env.example .env
docker-compose up -d
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py load_benchmarks
docker-compose exec web python manage.py createsuperuser

# Run
docker-compose up
```

**Access:**
- Admin: http://localhost:8000/admin/
- API Docs: http://localhost:8000/api/docs/
- Evaluation UI: http://localhost:8000/templates/evaluation.html

---

## How It Works

```
┌─────────────────────────────────────────────────────────────┐
│                    CLIENT SUBMITS MODEL                      │
│  POST /api/v1/evaluations/                                  │
│  {benchmark_id: 1, model_endpoint: "https://api.com/predict"}│
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                  PLATFORM EVALUATES                         │
│  • Sends 62 African test questions to model                 │
│  • Scores responses (context, language, safety)             │
│  • Generates detailed report                                │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                    CLIENT GETS RESULTS                       │
│  {overall_score: 82.5, by_category: {mobile_money: 94}}    │
└─────────────────────────────────────────────────────────────┘
```

---

## API Examples

### Evaluate a Model

```bash
curl -X POST http://localhost:8000/api/v1/evaluations/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "benchmark_id": 1,
    "model_name": "My Banking Chatbot",
    "model_endpoint": "https://api.mymodel.com/predict",
    "model_api_key": "sk-abc123"
  }'
```

### Get Report

```bash
curl http://localhost:8000/api/v1/evaluations/1/report/ \
  -H "Authorization: Bearer YOUR_TOKEN"
```

---

## Benchmarks

| Country | Tests | Categories |
|---------|-------|------------|
| Senegal | 22 | Mobile Money, Wolof, Culture, Admin |
| Nigeria | 19 | Fintech, Pidgin, Culture, Security |
| Kenya | 21 | M-Pesa, Sheng, Culture, Health |

---

## Tech Stack

- **Backend:** Django 5 + DRF
- **Database:** PostgreSQL 16
- **Cache:** Redis
- **Tasks:** Celery
- **Storage:** MinIO (S3-compatible)
- **Container:** Docker

---

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Add Your Country's Benchmark

1. Create `evaluation/benchmarks/yourcountry.py`
2. Add 20+ test cases
3. Run `python manage.py load_benchmarks`

---

## Roadmap

- [ ] Add more African countries (Ghana, Tanzania, Ethiopia...)
- [ ] Voice data collection
- [ ] Image datasets for computer vision
- [ ] Real-time evaluation dashboard
- [ ] Mobile app for workers

---

## License

**Non-Commercial License** - Free for learning, research, and open-source contribution.

Commercial use requires written permission from Moussoum Defar.

See [LICENSE](LICENSE) for full details.

To request commercial license: contact@moussoumdefar.com

---

## Support

- Documentation: /api/docs/
- Issues: GitHub Issues
- Email: contact@moussoumdefar.com

---

**Built with for Africa**
