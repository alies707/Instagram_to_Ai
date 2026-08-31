# Instagram_to_Ai

## English Documentation

AI powered Instagram Business automation platform built with Python, FastAPI and OpenAI.

## Features

- Instagram Business API integration
- AI caption generation
- Automated publishing pipeline
- Content scheduling
- Analytics foundation
- Telegram automation foundation

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
PostgreSQL + Redis
        |
Celery Workers
```

## Technology Stack

- Python 3.12
- FastAPI
- PostgreSQL
- Redis
- Celery
- OpenAI API
- Meta Instagram Graph API
- Docker

## Installation

```bash
git clone https://github.com/alies707/Instagram_to_Ai.git
cd Instagram_to_Ai
cp .env.example .env
docker compose up --build
```

## Roadmap

- Meta OAuth production flow
- Secure token encryption
- Full publishing workflow
- Comment management
- Insights dashboard
- Telegram admin panel

---

# مستندات فارسی

## معرفی پروژه

Instagram_to_Ai یک سیستم هوشمند مدیریت اکانت Business اینستاگرام است که با Python ساخته می‌شود و قابلیت اتصال به هوش مصنوعی OpenAI را دارد.

## امکانات

- اتصال به Instagram Business API
- تولید کپشن با هوش مصنوعی
- انتشار خودکار محتوا
- زمان‌بندی پست‌ها
- تحلیل محتوا
- آماده‌سازی مدیریت کامنت و پنل مدیریتی

## معماری

```
Instagram Business
        |
Meta Graph API
        |
FastAPI
        |
OpenAI
        |
PostgreSQL + Redis
        |
Celery
```

## نصب

```bash
git clone https://github.com/alies707/Instagram_to_Ai.git
cd Instagram_to_Ai
cp .env.example .env
docker compose up --build
```

## مسیر توسعه

- تکمیل OAuth متا
- رمزنگاری Tokenها
- انتشار کامل پست
- مدیریت کامنت
- داشبورد تحلیل
- کنترل با Telegram Bot
