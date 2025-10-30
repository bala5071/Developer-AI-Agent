"""Code execution and validation tools"""
import subprocess
import sys
from pathlib import Path
from crewai.tools import tool


@tool("Execute Python code")
def execute_python(file_path: str) -> str:
    """Executes Python code and returns output"""
    try:
        result = subprocess.run(
            [sys.executable, file_path],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        output = f"STDOUT:\n{result.stdout}\n"
        if result.stderr:
            output += f"STDERR:\n{result.stderr}\n"
        output += f"Return Code: {result.returncode}"
        
        return output
    except subprocess.TimeoutExpired:
        return "Execution timed out after 30 seconds"
    except Exception as e:
        return f"Error executing Python code: {str(e)}"


@tool("Validate Python syntax")
def validate_syntax(file_path: str) -> str:
    """Validates Python code syntax without executing"""
    try:
        with open(file_path, 'r') as f:
            code = f.read()
        
        compile(code, file_path, 'exec')
        return f"✓ Code syntax is valid: {file_path}"
    except SyntaxError as e:
        return f"✗ Syntax Error in {file_path}:\nLine {e.lineno}: {e.msg}"
    except Exception as e:
        return f"Error validating code: {str(e)}"


@tool("Install dependencies")
def install_dependencies(requirements_file: str) -> str:
    """Installs Python dependencies from requirements.txt"""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", requirements_file],
            capture_output=True,
            text=True,
            timeout=300
        )
        
        if result.returncode == 0:
            return f"✓ Successfully installed dependencies from {requirements_file}"
        else:
            return f"✗ Error installing dependencies:\n{result.stderr}"
    except Exception as e:
        return f"Error installing dependencies: {str(e)}"


@tool("Execute shell command")
def execute_command(command: str, working_dir: str = ".") -> str:
    """Executes shell commands in the project directory"""
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=60,
            cwd=working_dir
        )
        
        output = f"Command: {command}\n"
        output += f"STDOUT:\n{result.stdout}\n"
        if result.stderr:
            output += f"STDERR:\n{result.stderr}\n"
        output += f"Return Code: {result.returncode}"
        
        return output
    except Exception as e:
        return f"Error executing command: {str(e)}"