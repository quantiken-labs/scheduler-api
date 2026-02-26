from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from datetime import datetime
import uuid

scheduler = BackgroundScheduler()
scheduler.start()

jobs = {}

def test_task(job_id: str, message: str):
    print(f"[{datetime.utcnow()}] Job {job_id}: {message}")

def add_interval_job(seconds: int, message: str):
    job_id = str(uuid.uuid4())
    job = scheduler.add_job(
        test_task,
        trigger=IntervalTrigger(seconds=seconds),
        args=[job_id, message],
        id=job_id,
        replace_existing=True,
    )
    jobs[job_id] = job
    return job_id

def remove_job(job_id: str):
    scheduler.remove_job(job_id)
    jobs.pop(job_id, None)

def list_jobs():
    return [
        {
            "job_id": job.id,
            "next_run_time": str(job.next_run_time),
        }
        for job in scheduler.get_jobs()
    ]
