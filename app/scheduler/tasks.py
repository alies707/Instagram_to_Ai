from app.scheduler.celery_app import celery_app


@celery_app.task(name="app.scheduler.tasks.publish_scheduled_posts")
def publish_scheduled_posts():
    # Database query and Instagram publishing integration will run here.
    return {"status": "scheduled_publish_worker_ready"}
