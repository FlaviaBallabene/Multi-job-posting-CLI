import sys
sys.path.insert(0, '/workspaces/multi-job-posting-CLI')

import typer
from cli.commands.post_job import post_job_command

app = typer.Typer(help="Multi Job Posting CLI - Post jobs to multiple boards")

app.command()(post_job_command)

if __name__ == "__main__":
    app()