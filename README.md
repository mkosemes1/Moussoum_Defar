# Moussoum Defar

**Data and AI infrastructure for Africa**

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.0+-green.svg)](https://djangoproject.com)
[![License](https://img.shields.io/badge/License-Non--Commercial-blue.svg)](LICENSE)

---

## The Problem

I built this because I see the limit of the existing AIs, every time we tested an AI model with African context, it failed or it can't be as goodas in the West.

Try asking a chatbot about our means of payment or our finances or even in relation to our educational evolution - it doesn't know what you're talking about. Ask it to understand Wolof mixed with French - it's lost. Ask about FCFA or how to get a birth certificate in Dakar - nothing.

The AI industry has a blind spot: Africa. All the data, benchmarks, and tools are built for Western contexts. We're just... not part of the conversation.

## Why This Exists

Moussoum Defar is my attempt to fix this. It's a platform where:

- African workers collect real data from real communities ( student, linguist, or expert)
- AI models get tested against African benchmarks (not just translated Western ones)
- We build the infrastructure that's been missing since the AI Boom

I started with 3 countries (Senegal, Nigeria, Kenya) and 62 test cases. But the goal is to cover the whole continent.

---

## What It Does

### Data Collection
Real people, real data. Workers across Africa get paid to collect text, voice, and images in their own languages and communities. No more scraping the internet for "African data."

### AI Evaluation
You have an AI model? Test it. Send it through 62 African test cases and see if it actually understands the context. Not just "does it speak French?" but "does it understand what a senegalese person means when they say 'Nanga def?'"

### Worker System
Students, linguists, experts - they all earn money by contributing to better AI. There's a scoring system, levels, the whole gamification thing. The better you are, the more you earn.

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

To request commercial license: malickoseme@gmail.com

---

## Support

- Documentation: /api/docs/
- Issues: GitHub Issues
- Email: malickoseme@gmail.com

---

**Made in Africa, for Africa.**

If you want to help, open an issue or send me an email.
