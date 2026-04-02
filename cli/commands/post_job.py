import typer
import json
from adapters.linkedin import LinkedInAdapter
from adapters.workday import WorkdayAdapter
from adapters.bamboohr import BambooHRAdapter
from cli.utils.helpers import load_job_file

def post_job_command(
    file: str = typer.Option(..., help="Path to job JSON file"),
    boards: str = typer.Option(..., help="Comma-separated list of boards: linkedin,workday,bamboohr")
):
    """
    Post a job to multiple job boards
    """
    job_data = load_job_file(file)
    selected_boards = [b.strip().lower() for b in boards.split(",")]
    typer.echo(f"Posting to boards: {selected_boards}")
    
    results = {}

    for board in selected_boards:
        if board == "linkedin":
            adapter = LinkedInAdapter()
        elif board == "workday":
            adapter = WorkdayAdapter()
        elif board == "bamboohr":
            adapter = BambooHRAdapter()
        else:
            typer.echo(f"[WARNING] Unknown board: {board}")
            continue

        try:
            response = adapter.post_job(job_data)
            results[board] = response
            typer.echo(f"[SUCCESS] Posted job to {board}: {response.get('job_url')}")
        except Exception as e:
            results[board] = {"error": str(e)}
            typer.echo(f"[ERROR] Failed to post to {board}: {e}")

    typer.echo("\nSummary:")
    typer.echo(json.dumps(results, indent=2))