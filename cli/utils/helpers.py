import json

def load_job_file(file_path: str) -> dict:
    """Load job data from a JSON file"""
    with open(file_path, "r") as f:
        return json.load(f)