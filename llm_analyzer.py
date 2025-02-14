import openai
import json
import logging

def analyze_file_with_llm(file_path):
    """
    Analyze the given file for refactoring suggestions using an LLM.
    Returns a list of suggestions with keys: "issue", "suggestion", and "priority".
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()
    except Exception as e:
        logging.error("Unable to read file %s: %s", file_path, e)
        return []

    prompt = f"""
You are a coding assistant focused on improving code maintainability and productivity.
Analyze the following Python code and propose any necessary refactorings that adhere to best practices.
Do not introduce any breaking changes. For each suggestion, provide a JSON object with the following keys:
  - "issue": a brief description of the code issue.
  - "suggestion": the proposed refactoring.
  - "priority": one of "High", "Medium", or "Low", where High indicates a strong impact.
Return the suggestions as a JSON array.
Here is the code:
```
{code}
```
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful coding assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=600,
        )
        reply = response.choices[0].message.content.strip()
        suggestions = json.loads(reply)
        if not isinstance(suggestions, list):
            suggestions = []
        return suggestions
    except Exception as e:
        logging.error("LLM analysis failed for file %s: %s", file_path, e)
        return []

def evaluate_suggestions(suggestions):
    """
    Evaluate and prioritize the suggestions.
    Priority mapping: High -> 3, Medium -> 2, Low -> 1.
    Returns the sorted list of suggestions.
    """
    priority_map = {"High": 3, "Medium": 2, "Low": 1}
    for s in suggestions:
        if s.get("priority") not in priority_map:
            s["priority"] = "Medium"
    suggestions.sort(key=lambda s: priority_map.get(s["priority"], 2), reverse=True)
    return suggestions 