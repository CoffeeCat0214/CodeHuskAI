import logging
from repo_manager import clone_or_pull_repo
from code_analyzer import analyze_codebase
from refactoring import apply_refactorings
from config import REPO_URL, LOCAL_REPO_PATH

def run_agent():
    logging.info("Cloning or pulling repository: %s", REPO_URL)
    repo_path = clone_or_pull_repo(REPO_URL, LOCAL_REPO_PATH)
    logging.info("Analyzing codebase in %s", repo_path)
    refactorings = analyze_codebase(repo_path)
    if refactorings:
        logging.info("Applying refactorings...")
        apply_refactorings(repo_path, refactorings)
    else:
        logging.info("No refactorings required.") 