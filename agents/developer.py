# from crewai import Agent
# from tools.file_operations import write_file, read_file, create_directory, list_directory
# from tools.code_execution import validate_syntax, install_dependencies
# from config import AGENT_VERBOSE


# def create_developer_agent():
#     return Agent(
#     role="Senior Software Developer",
#     goal="Write clean, efficient, and well-documented code based on technical specifications",
#     backstory="""You are a senior full-stack developer with expertise in multiple 
#         programming languages and frameworks. You write production-ready code following 
#         best practices, SOLID principles, and industry standards. You create modular, 
#         maintainable code with proper error handling and documentation.""",
#     llm="ollama/codellama:13b-instruct",
#     verbose=AGENT_VERBOSE,
#     tools=[
#         write_file,
#         read_file,
#         create_directory,
#         list_directory,
#         validate_syntax,
#         install_dependencies
#     ],
#     allow_delegation=False,
#     max_iter=15
# )


"""Enhanced Developer Agent with Detailed Instructions"""
from crewai import Agent
from tools.file_operations import write_file, read_file, create_directory, list_directory, append_to_file, copy_item, move_item, delete_item, get_file_info, search_files, create_from_template
from tools.code_execution import validate_syntax, install_dependencies, execute_code, run_tests, format_code, lint_code, build_project
from config import AGENT_VERBOSE

dev_backstory = """You are an experienced software engineer who writes high-quality code \
        following best practices and industry standards. You focus on creating robust solutions \
        with proper error handling and documentation."""

def create_developer_agent():
    return Agent(
        role="Senior Full-Stack Software Engineer",
        
        goal="""Write clean, efficient, and maintainable code based on detailed technical specifications.""",
        backstory=dev_backstory,
        verbose=AGENT_VERBOSE,
        tools=[
            write_file, read_file, create_directory, list_directory,
            validate_syntax, install_dependencies, append_to_file, 
            copy_item, move_item, delete_item, get_file_info, 
            search_files, create_from_template, execute_code, 
            run_tests, format_code, lint_code, build_project
        ],
        allow_delegation=False,
        max_iter=20  # Increased for thorough implementation
    )