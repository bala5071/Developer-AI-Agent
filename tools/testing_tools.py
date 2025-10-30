"""Testing and quality assurance tools"""
import subprocess
import sys
from pathlib import Path
from crewai.tools import tool


@tool("Run pytest tests")
def run_tests(directory: str) -> str:
    """Runs pytest tests in the project"""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", "-v"],
            capture_output=True,
            text=True,
            timeout=300,
            cwd=directory
        )
        
        output = "=== TEST RESULTS ===\n"
        output += result.stdout
        if result.stderr:
            output += f"\nErrors:\n{result.stderr}"
        
        if result.returncode == 0:
            output += "\n✓ All tests passed!"
        else:
            output += "\n✗ Some tests failed"
        
        return output
    except subprocess.TimeoutExpired:
        return "Tests timed out after 300 seconds"
    except Exception as e:
        return f"Error running tests: {str(e)}"


@tool("Format Python code")
def format_code(directory: str) -> str:
    """Formats Python code using Black"""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "black", directory],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        if result.returncode == 0:
            return f"✓ Code formatted successfully:\n{result.stdout}"
        else:
            return f"✗ Formatting errors:\n{result.stderr}"
    except Exception as e:
        return f"Error formatting code: {str(e)}"


@tool("Lint Python code")
def lint_code(directory: str) -> str:
    """Lints Python code for style issues"""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "flake8", directory, "--max-line-length=120"],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        if result.returncode == 0:
            return "✓ No linting issues found"
        else:
            return f"Linting issues found:\n{result.stdout}"
    except Exception as e:
        return f"Error linting code: {str(e)}"


@tool("Generate test file")
def generate_test(file_path: str, module_name: str) -> str:
    """Creates a basic test file template"""
    try:
        test_content = f'''"""Tests for {module_name}"""
import pytest
from {module_name} import *


def test_example():
    """Example test case"""
    assert True, "This test should pass"


# Add more test cases here
'''
        
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, 'w') as f:
            f.write(test_content)
        
        return f"✓ Test file created: {file_path}"
    except Exception as e:
        return f"Error creating test file: {str(e)}"