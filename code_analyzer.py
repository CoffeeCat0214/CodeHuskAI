import os
import logging
from llm_analyzer import analyze_file_with_llm, evaluate_suggestions

def analyze_codebase(repo_path):
    """
    Analyze the given codebase using an LLM for best practices.
    This function scans for .py files and for each file uses the LLM to propose
    refactorings. Suggestions are evaluated and prioritized.
    Returns a list of refactoring suggestions with file path, issue, suggestion, and priority.
    """
    all_suggestions = []
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                logging.info("Analyzing file: %s", file_path)
                suggestions = analyze_file_with_llm(file_path)
                if suggestions:
                    evaluated = evaluate_suggestions(suggestions)
                    for s in evaluated:
                        s["file"] = file_path
                        all_suggestions.append(s)
    # Sort all suggestions by overall priority across the codebase
    priority_map = {"High": 3, "Medium": 2, "Low": 1}
    all_suggestions.sort(key=lambda s: priority_map.get(s["priority"], 2), reverse=True)
    return all_suggestions 