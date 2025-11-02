# """QA Tester Agent"""
# from crewai import Agent
# from tools.testing_tools import run_tests, format_code, lint_code, generate_test
# from tools.code_execution import execute_python, validate_syntax
# from tools.file_operations import read_file, write_file
# from config import AGENT_VERBOSE


# def create_tester_agent():
#     return Agent(
#         role="QA Engineer & Test Specialist",
#         goal="Ensure code quality through comprehensive testing and validation",
#         backstory="""You are a meticulous QA engineer with expertise in test-driven 
#         development, automated testing, and quality assurance. You write comprehensive 
#         test suites, identify edge cases, and ensure code reliability. You use pytest, 
#         unit testing, integration testing, and follow testing best practices.""",
#         llm="ollama/codellama:13b-instruct",
#         verbose=AGENT_VERBOSE,
#         tools=[
#             run_tests,
#             format_code,
#             lint_code,
#             generate_test,
#             execute_python,
#             validate_syntax,
#             read_file,
#             write_file
#         ],
#         allow_delegation=False,
#         max_iter=15
#     )


"""Enhanced QA Tester Agent with Comprehensive Testing Standards"""
from crewai import Agent
from tools.testing_tools import run_tests, run_tests_with_coverage, format_code, lint_code, generate_test_file
from tools.code_execution import execute_code, validate_syntax
from tools.file_operations import write_file, read_file, create_directory, list_directory, append_to_file, copy_item, move_item, delete_item, get_file_info, search_files, create_from_template
from config import AGENT_VERBOSE


def create_tester_agent():
    return Agent(
        role="QA Engineer & Test Specialist",
        goal="Ensure code quality through comprehensive testing and validation",
        backstory="You are a meticulous QA engineer who ensures code reliability through thorough testing and validation.",
        verbose=AGENT_VERBOSE,
        tools=[
            run_tests, format_code, lint_code, generate_test_file,
            execute_code, validate_syntax, read_file, write_file,
            append_to_file, run_tests_with_coverage, create_directory,
            list_directory, copy_item, move_item, delete_item,
            get_file_info, search_files, create_from_template
        ],
        allow_delegation=False,
        max_iter=20
    )