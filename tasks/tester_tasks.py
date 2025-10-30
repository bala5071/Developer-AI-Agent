"""Testing Tasks"""
from crewai import Task


def create_testing_task(agent, project_dir: str, context_tasks: list = None):
    return Task(
        description=f"""Test and validate the implemented project:

PROJECT DIRECTORY: {project_dir}

Your responsibilities:
1. Review all code files for:
   - Syntax errors
   - Logic issues
   - Best practices compliance
   - Code quality
2. Create comprehensive test files:
   - Unit tests for all functions/classes
   - Integration tests if applicable
   - Edge case testing
   - Error handling tests
3. Run all tests using Pytest
4. Format code using Black
5. Lint code using Flake8
6. Execute the main program to verify it works
7. Document any issues found
8. Suggest fixes if problems are detected
9. Create a TEST_REPORT.md with results

IMPORTANT:
- Use Test Generator tool to create test files
- Use Pytest Runner to execute tests
- Use Code Formatter to format code
- Use Linter to check code style
- Use Python Executor to run the main program
- Document all test results

Ensure the project is production-ready and all tests pass.""",
        agent=agent,
        context=context_tasks,
        expected_output="""Complete testing report including:
- Test file creation summary
- Test execution results
- Code formatting results
- Linting results
- Main program execution output
- List of any issues found
- Overall quality assessment
- TEST_REPORT.md file"""
    )