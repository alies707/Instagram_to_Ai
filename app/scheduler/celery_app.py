import os
from celery import Celery

celery_app = Celery(
    "instagram_ai",
    broker=os.getenv("REDIS_URL", "redis://localhost:6379/0"),
    backend=os.getenv("REDIS_URL", "redis://localhost:6379/0")
)

celery_app.conf.timezone = "UTC"
celery_app.conf.beat_schedule = {
    "publish-scheduled-posts": {
        "task": "app.scheduler.tasks.publish_scheduled_posts",
        "schedule": 60.0,
    }
}
