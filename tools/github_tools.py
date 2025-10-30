"""GitHub integration tools"""
from github import Github
from git import Repo
from pathlib import Path
from crewai.tools import tool
from config import GITHUB_TOKEN, GITHUB_USERNAME


@tool("Create GitHub repository")
def create_github_repo(repo_name: str, description: str = "", private: bool = False) -> str:
    """Creates a new GitHub repository"""
    try:
        if not GITHUB_TOKEN:
            return "Error: GitHub token not configured. Set GITHUB_TOKEN in .env"
        
        g = Github(GITHUB_TOKEN)
        user = g.get_user()
        
        repo = user.create_repo(
            name=repo_name,
            description=description,
            private=private,
            auto_init=False
        )
        
        return f"✓ Repository created: {repo.html_url}"
    except Exception as e:
        return f"Error creating GitHub repository: {str(e)}"


@tool("Initialize Git repository")
def init_git(directory: str) -> str:
    """Initializes a Git repository in a directory"""
    try:
        repo = Repo.init(directory)
        return f"✓ Git repository initialized in {directory}"
    except Exception as e:
        return f"Error initializing Git repository: {str(e)}"


@tool("Commit changes to Git")
def commit_changes(directory: str, message: str) -> str:
    """Commits all changes in the repository"""
    try:
        repo = Repo(directory)
        repo.git.add(A=True)
        repo.index.commit(message)
        return f"✓ Changes committed: {message}"
    except Exception as e:
        return f"Error committing changes: {str(e)}"


@tool("Push to GitHub")
def push_to_github(directory: str, repo_url: str) -> str:
    """Pushes commits to GitHub"""
    try:
        repo = Repo(directory)
        
        # Add remote if it doesn't exist
        if 'origin' not in [remote.name for remote in repo.remotes]:
            repo.create_remote('origin', repo_url)
        
        origin = repo.remote('origin')
        
        # Push to main/master branch
        current_branch = repo.active_branch.name
        origin.push(refspec=f'{current_branch}:{current_branch}')
        
        return f"✓ Successfully pushed to {repo_url}"
    except Exception as e:
        return f"Error pushing to GitHub: {str(e)}"


@tool("Complete GitHub deployment")
def deploy_to_github(directory: str, repo_name: str, description: str = "", 
                     commit_message: str = "Initial commit") -> str:
    """Complete GitHub workflow: init, commit, create repo, and push"""
    try:
        if not GITHUB_TOKEN or not GITHUB_USERNAME:
            return "Error: GitHub credentials not configured. Set GITHUB_TOKEN and GITHUB_USERNAME in .env"
        
        results = []
        
        # Initialize Git
        repo = Repo.init(directory)
        results.append("✓ Git initialized")
        
        # Create .gitignore
        gitignore_path = Path(directory) / ".gitignore"
        if not gitignore_path.exists():
            with open(gitignore_path, 'w') as f:
                f.write("__pycache__/\n*.pyc\n.env\n*.log\nvenv/\n.vscode/\n")
            results.append("✓ .gitignore created")
        
        # Commit changes
        repo.git.add(A=True)
        repo.index.commit(commit_message)
        results.append(f"✓ Changes committed: {commit_message}")
        
        # Create GitHub repository
        g = Github(GITHUB_TOKEN)
        user = g.get_user()
        gh_repo = user.create_repo(
            name=repo_name,
            description=description,
            private=False,
            auto_init=False
        )
        results.append(f"✓ GitHub repository created: {gh_repo.html_url}")
        
        # Add remote and push
        repo_url = f"https://{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/{repo_name}.git"
        
        if 'origin' not in [remote.name for remote in repo.remotes]:
            repo.create_remote('origin', repo_url)
        
        origin = repo.remote('origin')
        origin.push(refspec='master:master')
        results.append("✓ Code pushed to GitHub")
        
        return "\n".join(results) + f"\n\nRepository URL: {gh_repo.html_url}"
        
    except Exception as e:
        return f"Error in GitHub deployment: {str(e)}"