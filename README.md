# Instagram_to_Ai

AI powered Instagram Business automation platform.

## Stack
- Python
- FastAPI
- PostgreSQL
- Redis
- Celery
- OpenAI API
- Meta Instagram Graph API
- Telegram Admin Bot (planned)

## Architecture
```
Instagram Business
        |
Meta Graph API
        |
FastAPI Backend
        |
OpenAI API
        |
Database + Scheduler
```

## Features roadmap

### Phase 1
- Meta API integration structure
- Token management
- Account information
- Publishing pipeline

### Phase 2
- AI caption generation
- Hashtag generation
- Content analysis

### Phase 3
- Comment management
- Insights reports
- Telegram control

## Run

Copy `.env.example` to `.env` and configure credentials.

```
docker compose up --build
```
