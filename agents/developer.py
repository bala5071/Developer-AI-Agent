from crewai import Agent
from tools.file_operations import write_file, read_file, create_directory, list_directory
from tools.code_execution import validate_syntax, install_dependencies
from config import AGENT_VERBOSE


def create_developer_agent():
    return Agent(
    role="Senior Software Developer",
    goal="Write clean, efficient, and well-documented code based on technical specifications",
    backstory="""You are a senior full-stack developer with expertise in multiple 
        programming languages and frameworks. You write production-ready code following 
        best practices, SOLID principles, and industry standards. You create modular, 
        maintainable code with proper error handling and documentation.""",
    llm="ollama/llama3",
    verbose=AGENT_VERBOSE,
    tools=[
        write_file,
        read_file,
        create_directory,
        list_directory,
        validate_syntax,
        install_dependencies
    ],
    allow_delegation=False,
    max_iter=15
)