"""File operation tools for agents"""
import os
import json
from pathlib import Path
from typing import Dict, List, Type
from pydantic import BaseModel, Field
from crewai.tools import tool


@tool("Write content to a file")
def write_file(file_path: str, content: str) -> str:
    """Writes content to a file in the project directory"""
    try:
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return f"Successfully wrote to {file_path}"
    except Exception as e:
        return f"Error writing file: {str(e)}"


@tool("Read content from a file")
def read_file(file_path: str) -> str:
    """Reads content from a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except Exception as e:
        return f"Error reading file: {str(e)}"


@tool("Create a directory")
def create_directory(directory_path: str) -> str:
    """Creates a directory structure"""
    try:
        Path(directory_path).mkdir(parents=True, exist_ok=True)
        return f"Successfully created directory: {directory_path}"
    except Exception as e:
        return f"Error creating directory: {str(e)}"


@tool("List files in a directory")
def list_directory(directory_path: str) -> str:
    """Lists all files and directories in a given path"""
    try:
        path = Path(directory_path)
        if not path.exists():
            return f"Directory does not exist: {directory_path}"
        
        items = []
        for item in path.rglob("*"):
            if item.is_file():
                relative_path = item.relative_to(path)
                items.append(f"FILE: {relative_path}")
        
        return "\n".join(items) if items else "Directory is empty"
    except Exception as e:
        return f"Error listing directory: {str(e)}"