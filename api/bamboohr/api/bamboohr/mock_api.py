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
    Mock BambooHR job posting
    """
    return {
        "job_url": f"https://bamboohr.mock/job/{uuid4()}",
        "status": "success"
    }