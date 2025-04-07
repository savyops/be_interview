import subprocess

def execute_untrusted_code(code: str) -> str:
    """Dangerous! Executes arbitrary Python code."""
    try:
        result = subprocess.run(
            ["python3", "-c", code],
            capture_output=True,
            text=True
        )
        return result.stdout
    except Exception as e:
        return f"Error: {e}"