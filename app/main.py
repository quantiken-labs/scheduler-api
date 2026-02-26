from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from scheduler import add_interval_job, remove_job, list_jobs

app = FastAPI(title="Scheduler API (Test Version)")

class JobRequest(BaseModel):
    seconds: int
    message: str

@app.post("/schedule")
def schedule_job(job: JobRequest):
    if job.seconds < 5:
        raise HTTPException(status_code=400, detail="Minimum interval is 5 seconds (test safety)")
    job_id = add_interval_job(job.seconds, job.message)
    return {"job_id": job_id}

@app.get("/jobs")
def get_jobs():
    return list_jobs()

@app.delete("/jobs/{job_id}")
def delete_job(job_id: str):
    remove_job(job_id)
    return {"status": "deleted", "job_id": job_id}
