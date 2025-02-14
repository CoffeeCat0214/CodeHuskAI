import os
import logging
from git import Repo, InvalidGitRepositoryError

def clone_or_pull_repo(repo_url, local_repo_path):
    if os.path.exists(local_repo_path):
        try:
            repo = Repo(local_repo_path)
            logging.info("Repository already exists. Pulling latest changes...")
            repo.remotes.origin.pull()
        except InvalidGitRepositoryError:
            logging.error("Directory exists but is not a git repository: %s", local_repo_path)
            raise
    else:
        logging.info("Cloning repository from %s into %s", repo_url, local_repo_path)
        repo = Repo.clone_from(repo_url, local_repo_path)
    return local_repo_path 