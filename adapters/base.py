from abc import ABC, abstractmethod

class BaseAdapter(ABC):
    """Abstract base class for job board adapters"""

    @abstractmethod
    def post_job(self, job_data: dict) -> dict:
        """
        Post a job to the board
        Returns a dict with at least a 'job_url' key on success
        """
        pass