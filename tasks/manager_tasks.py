"""Planning Tasks"""
from crewai import Task


def create_planning_task(agent, project_description: str, project_type: str = "python"):
    return Task(
        description=f"""Analyze the following project requirement and create a comprehensive technical plan:

                        PROJECT DESCRIPTION:
                        {project_description}

                        PROJECT TYPE: {project_type}

                        Your planning must include:
                        1. Project Overview and Objectives
                        2. Technology Stack Selection (libraries, frameworks, tools)
                        3. Project Structure (directories, files, modules)
                        4. Key Components and Features
                        5. Data Models/Schema (if applicable)
                        6. API Design (if applicable)
                        7. Implementation Steps (detailed breakdown)
                        8. Potential Challenges and Solutions
                        9. Testing Strategy
                        10. Documentation Requirements

                        Provide a DETAILED technical specification that a developer can follow to implement the project.
                        Include specific file names, module structures, and implementation guidelines.""",
        agent=agent,
        expected_output="""A comprehensive technical plan document containing:
                            - Complete project architecture
                            - File and directory structure
                            - Technology stack with specific versions
                            - Detailed implementation steps
                            - Testing strategy
                            - All necessary technical specifications"""
    )