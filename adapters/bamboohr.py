import requests
from adapters.base import BaseAdapter

class BambooHRAdapter(BaseAdapter):
    """Adapter for BambooHR (mocked API)"""

    API_URL = "http://localhost:8000/bamboohr/post"

    def post_job(self, job_data: dict) -> dict:
        response = requests.post(self.API_URL, json=job_data)
        response.raise_for_status()
        return response.json()