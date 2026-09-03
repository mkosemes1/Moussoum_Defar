# African AI Platform

Infrastructure de données et d'intelligence IA pour l'Afrique.

## Vue d'ensemble

Cette plateforme fournit une infrastructure spécialisée pour comprendre, mesurer et améliorer l'IA dans les contextes africains. Elle se compose de trois piliers principaux :

### 1. African Data Hub
- Collecte locale de données (texte, voix, images)
- Workers africains rémunérés pour la collecte
- Système de qualité et de validation
- Datasets prêts à l'emploi pour les entreprises IA

### 2. AI Evaluation Lab
- Tests de modèles IA contre des benchmarks africains
- Évaluation de la compréhension contextuelle
- Rapports détaillés par pays et par catégorie
- API pour intégration automatisée

### 3. AI Workforce
- Réseau de workers africains (étudiants, linguistes, experts)
- Système de niveaux et de réputation
- Rémunération via Mobile Money
- Économie de compétences autour de l'IA

## Architecture Technique

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

## Stack Technique

| Composant | Choix | Coût/mois |
|---|---|---|
| Backend | Django 5 + Django REST Framework | 0$ |
| Base de données | PostgreSQL 16 | ~25$ |
| Cache + Queue | Redis | ~15$ |
| Fichiers | MinIO (self-hosted) | 0$ |
| Tâches async | Celery + Redis | 0$ |
| Serveur | Hetzner CX32 | ~10$ |
| SSL + Proxy | Caddy | 0$ |
| **Total** | | **~50$/mois** |

## Installation

### Prérequis

- Docker et Docker Compose installés
- Python 3.11+ (pour le développement local)
- Git

### Setup avec Docker (Recommandé)

```bash
# Cloner le repository
git clone <repository-url>
cd africai

# Copier le fichier d'environnement
cp .env.example .env

# Démarrer les services
docker-compose up -d

# Créer la base de données et les tables
docker-compose exec web python manage.py migrate

# Créer un superuser
docker-compose exec web python manage.py createsuperuser

# Lancer le serveur de développement
docker-compose up
```

### Setup local (Sans Docker)

```bash
# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Configurer la base de données
# Modifier les paramètres dans africai/settings.py

# Lancer les migrations
python manage.py migrate

# Créer un superuser
python manage.py createsuperuser

# Lancer le serveur
python manage.py runserver
```

## Structure du Projet

```
africai/
├── africai/                 # Configuration Django
│   ├── settings.py          # Paramètres principaux
│   ├── urls.py              # URLs racines
│   ├── wsgi.py              # WSGI
│   └── asgi.py              # ASGI
├── workers/                 # Module Data Hub + Workforce
│   ├── models.py            # Modèles Worker, Collection, etc.
│   ├── serializers.py       # Sérialiseurs API
│   ├── views.py             # Vues API
│   ├── urls.py              # Routes API
│   ├── admin.py             # Administration
│   └── scoring.py           # Système de scoring
├── evaluation/              # Module AI Evaluation Lab
│   ├── models.py            # Modèles Benchmark, Evaluation, etc.
│   ├── serializers.py       # Sérialiseurs API
│   ├── views.py             # Vues API
│   ├── urls.py              # Routes API
│   ├── admin.py             # Administration
│   ├── scoring.py           # Système de scoring IA
│   └── benchmarks/          # Benchmarks africains
│       ├── senegal.py       # Benchmark Sénégal
│       ├── nigeria.py       # Benchmark Nigeria
│       └── kenya.py         # Benchmark Kenya
├── clients/                 # Module Client
│   ├── models.py            # Modèles Client, Subscription
│   ├── serializers.py       # Sérialiseurs API
│   ├── views.py             # Vues API
│   ├── urls.py              # Routes API
│   └── admin.py             # Administration
├── templates/               # Templates HTML
├── static/                  # Fichiers statiques
├── docker-compose.yml       # Orchestration Docker
├── Dockerfile               # Image Docker
├── requirements.txt         # Dépendances Python
└── .env.example             # Variables d'environnement
```

## API Endpoints

### Authentication

```
POST   /api/v1/auth/register/           → Inscription
POST   /api/v1/auth/login/              → Connexion
POST   /api/v1/auth/refresh/            → Rafraîchir le token
```

### Workers (Data Hub)

```
GET    /api/v1/workers/me/              → Profil worker
PUT    /api/v1/workers/me/              → Mettre à jour le profil
GET    /api/v1/workers/me/score/        → Score qualité
GET    /api/v1/workers/me/tasks/        → Tâches assignées
GET    /api/v1/workers/me/earnings/     → Gains
GET    /api/v1/collections/             → Projets disponibles
POST   /api/v1/collections/{id}/submit/ → Soumettre une donnée
```

### Evaluation Lab

```
GET    /api/v1/benchmarks/              → Liste des benchmarks
GET    /api/v1/benchmarks/{id}/         → Détails d'un benchmark
GET    /api/v1/benchmarks/{id}/tests/   → Cas de test
POST   /api/v1/evaluations/             → Créer une évaluation
GET    /api/v1/evaluations/{id}/        → Résultats
GET    /api/v1/evaluations/{id}/report/ → Rapport détaillé
POST   /api/v1/models/test/             → Test rapide d'un modèle
```

### Clients

```
GET    /api/v1/clients/me/              → Profil client
GET    /api/v1/clients/me/usage/        → Utilisation
POST   /api/v1/clients/me/subscription/ → Gérer l'abonnement
```

## Développement

### Lancer les tests

```bash
# Tous les tests
docker-compose exec web python manage.py test

# Tests d'un module spécifique
docker-compose exec web python manage.py test workers
docker-compose exec web python manage.py test evaluation
```

### Ajouter un nouveau benchmark

1. Créer un fichier dans `evaluation/benchmarks/`
2. Définir les cas de test au format JSON
3. Enregistrer le benchmark dans la base de données

### Développer un nouveau endpoint

1. Ajouter le modèle dans `models.py`
2. Créer le sérialiseur dans `serializers.py`
3. Ajouter la vue dans `views.py`
4. Enregistrer la route dans `urls.py`

## Modèle de Données

### Workers

- **Worker** : Profil du travailleur africain
- **Language** : Langues parlées
- **WorkerScore** : Scores de compétence
- **QualityLog** : Historique de qualité

### Data Hub

- **DataCollection** : Projet de collecte
- **DataSubmission** : Soumission d'un worker

### Evaluation

- **AfricanBenchmark** : Benchmark par pays/contexte
- **TestCase** : Cas de test individuel
- **Evaluation** : Évaluation d'un modèle
- **TestExecution** : Exécution d'un test

### Clients

- **Client** : Entreprise utilisatrice
- **Subscription** : Abonnement
- **APIKey** : Clé d'accès API

## Sécurité

- Authentification JWT
- Rate limiting sur les API
- Validation des entrées
- Chiffrement des données sensibles
- Conformité RGPD

## Déploiement

### Production

```bash
# Construire l'image
docker-compose -f docker-compose.prod.yml build

# Déployer
docker-compose -f docker-compose.prod.yml up -d

# Appliquer les migrations
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate

# Collecter les fichiers statiques
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic
```

## Licence

Propriétaire - Tous droits réservés.

## Contact

Pour toute question : contact@africai.com
