# Multi-Job Posting Automation 

A unified automation framework for publishing job postings across multiple platforms—including LinkedIn, Workday, and BambooHR. Features include a Typer-based CLI, FastAPI mock services, a Streamlit GUI, integration tests, and storage for job history.

This project is a scalable, AI-friendly architecture for Recruiting technology automation, enabling both humans and bots to trigger consistent, repeatable job-posting workflows.

![alt text](<Multi-Job Posting Automation.png>)

## Features

- Post jobs via CLI (Typer-based)
- Mock APIs with FastAPI for testing
- Streamlit web interface for job posting
- Job history tracking with GET/DELETE endpoints
- Unit and integration tests
- Support for multiple job boards

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/FlaviaBallabene/multi-job-posting-CLI.git
   cd multi-job-posting-CLI
   ```

2. Install dependencies:
   ```bash
   pip install -e .
   ```

## Usage

### CLI

Post a job using the CLI:
```bash
multi-job-posting --file examples/sample_job.json --boards linkedin,workday,bamboohr
```

### API Server

Run the FastAPI server:
```bash
python api/server.py
```

Available endpoints:
- `POST /linkedin/post` - Post job to LinkedIn
- `POST /workday/post` - Post job to Workday
- `POST /bamboohr/post` - Post job to BambooHR
- `GET /jobs` - Get all posted jobs
- `DELETE /jobs` - Clear all posted jobs

Example API call:
```bash
curl -X POST http://localhost:8000/linkedin/post \
  -H "Content-Type: application/json" \
  -d @examples/sample_job.json
```

View posted jobs:
```bash
curl http://localhost:8000/jobs
```

Clear job history:
```bash
curl -X DELETE http://localhost:8000/jobs
```

### Streamlit GUI

Run the Streamlit GUI:
```bash
streamlit run gui/app.py
```

Upload a job JSON file, select boards, and post jobs with a user-friendly interface.

## Dependencies

- Python 3.8+
- Typer (CLI framework)
- FastAPI (API server)
- Uvicorn (ASGI server)
- Pydantic (data validation)
- Requests (HTTP client)
- Streamlit (web interface)
- Pytest (testing)

## Project Structure

```
multi-job-posting-cli/
├── cli/
│   ├── commands/
│   │   └── post_job.py
│   ├── utils/
│   │   └── helpers.py
│   └── main.py
├── api/
│   ├── bamboohr/
│   │   ├── api/
│   │   │   └── bamboohr/
│   │   │       └── mock_api.py
│   │   ├── __init__.py
│   │   └── mock_api.py
│   ├── linkedin/
│   │   ├── api/
│   │   │   └── linkedin/
│   │   │       └── mock_api.py
│   │   ├── __init__.py
│   │   └── mock_api.py
│   ├── workday/
│   │   ├── api/
│   │   │   └── workday/
│   │   │       └── mock_api.py
│   │   ├── __init__.py
│   │   └── mock_api.py
│   ├── __init__.py
│   ├── server.py
│   └── storage.py
├── adapters/
│   ├── base.py
│   ├── bamboohr.py
│   ├── linkedin.py
│   └── workday.py
├── examples/
│   ├── posting_notebook.ipynb
│   └── sample_job.json
├── gui/
│   └── app.py
├── pyproject.toml
├── README.md
└── requirements.txt
```