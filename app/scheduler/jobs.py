from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()


def schedule_post(task, run_time):
    scheduler.add_job(task, "date", run_date=run_time)


def start_scheduler():
    scheduler.start()
