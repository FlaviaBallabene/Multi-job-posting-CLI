from fastapi import APIRouter
from pydantic import BaseModel
from uuid import uuid4

router = APIRouter()

class JobPost(BaseModel):
    title: str
    location: str
    description: str
    department: str

@router.post("/post")
async def post_job(job: JobPost):
    """
    Mock Workday job posting
    """
    job_url = f"https://workday.mock/job/{uuid4()}"
    job_data = {
        "platform": "workday",
        "job_url": job_url,
        "status": "success",
        "job_details": job.dict()
    }
    
    # Import and add to global list
    from api.storage import posted_jobs
    posted_jobs.append(job_data)
    
    return {
        "job_url": job_url,
        "status": "success"
    }