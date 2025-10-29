from git import Repo
import os

def commit_and_push(repo_path, message):
    repo = Repo(repo_path)
    repo.git.add(A=True)
    repo.index.commit(message)
    origin = repo.remote(name='origin')
    origin.push()
    return "Code committed and pushed to GitHub."
