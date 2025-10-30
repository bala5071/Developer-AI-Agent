"""Development Tasks"""
from crewai import Task


def create_development_task(agent, project_dir: str, context_tasks: list = None):
    return Task(
        description=f"""Based on the technical plan, implement the complete project:

PROJECT DIRECTORY: {project_dir}

Your responsibilities:
1. Create the complete directory structure
2. Implement all source code files with proper documentation
3. Write a comprehensive README.md with:
   - Project description
   - Installation instructions
   - Usage examples
   - Feature list
   - Requirements
4. Create requirements.txt with all dependencies
5. Add example usage/demo files if applicable
6. Ensure all code follows best practices
7. Add inline comments and docstrings
8. Handle errors gracefully
9. Create configuration files if needed
10. Implement main execution file

IMPORTANT:
- Use the File Writer tool to create each file
- Use the Directory Creator tool to create folders
- Validate syntax using Code Validator tool
- Create complete, working, production-ready code
- Don't use placeholders - implement full functionality

Generate actual working code that solves the problem described in the plan.""",
        agent=agent,
        context=context_tasks,
        expected_output="""A complete, working project with:
- All source code files implemented
- README.md with comprehensive documentation
- requirements.txt with dependencies
- Proper project structure
- Example usage files
- All code validated and functional"""
    )