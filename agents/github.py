"""GitHub Manager Agent"""
from crewai import Agent
from tools.github_tools import (
    create_github_repo, init_git, commit_changes, 
    push_to_github, deploy_to_github
)
from tools.file_operations import write_file
from config import AGENT_VERBOSE


def create_github_agent():
    return Agent(
        role="GitHub Repository Manager",
        goal="Manage Git version control and deploy projects to GitHub",
        backstory="""You are a DevOps engineer specializing in Git workflows and 
        GitHub repository management. You handle version control, create repositories, 
        manage commits, and ensure proper project documentation. You follow Git best 
        practices and maintain clean commit histories.""",
        llm="ollama/llama3",
        verbose=AGENT_VERBOSE,
        tools=[
            create_github_repo,
            init_git,
            commit_changes,
            push_to_github,
            deploy_to_github,
            write_file
        ],
        allow_delegation=False,
        max_iter=10
    )