import sys
sys.path.insert(0, '/workspaces/multi-job-posting-CLI')

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.linkedin.mock_api import router as linkedin_router
from api.workday.mock_api import router as workday_router
from api.bamboohr.mock_api import router as bamboohr_router
from api.storage import posted_jobs

app = FastAPI(title="Mock Job Posting API")

# Allow all origins for testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(linkedin_router, prefix="/linkedin", tags=["LinkedIn"])
app.include_router(workday_router, prefix="/workday", tags=["Workday"])
app.include_router(bamboohr_router, prefix="/bamboohr", tags=["BambooHR"])

@app.get("/")
async def root():
    return {"message": "Mock Job Posting API", "docs": "/docs", "jobs": "/jobs"}

@app.get("/jobs")
async def get_posted_jobs():
    """Get all posted jobs"""
    return {"jobs": posted_jobs, "total": len(posted_jobs)}

@app.delete("/jobs")
async def clear_posted_jobs():
    """Clear all posted jobs"""
    posted_jobs.clear()
    return {"message": "All jobs cleared", "total": 0}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)