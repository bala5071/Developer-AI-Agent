"""GitHub Deployment Tasks"""
from crewai import Task


def create_github_task(agent, project_dir: str, github_username: str, repo_name: str, 
                       description: str, context_tasks: list = None):
    return Task(
        description=f"""Deploy the project to GitHub:

                        PROJECT DIRECTORY: {project_dir}
                        GITHUB USERNAME: {github_username}
                        REPOSITORY NAME: {repo_name}
                        DESCRIPTION: {description}

                        Your responsibilities:
                        1. Create a comprehensive .gitignore file
                        2. Create/update README.md with:
                           - Project badges (if applicable)
                           - Clear installation instructions
                           - Usage examples
                           - Features list
                           - License information
                        3. Initialize Git repository
                        4. Create initial commit with message: "Initial commit: {description}"
                        5. Create GitHub repository
                        6. Push all code to GitHub
                        7. Verify the repository is accessible
                        8. Create a DEPLOYMENT_REPORT.md with:
                           - Repository URL
                           - Deployment steps taken
                           - Any issues encountered
                           - Instructions for cloning and running

                        IMPORTANT:
                        - Use GitHub Full Deploy tool for complete workflow
                        - Ensure all files are committed
                        - Verify the push was successful
                        - Make sure README.md is comprehensive

                        Make the repository professional and ready for public viewing.""",
         agent=agent,
         context=context_tasks,
         expected_output="""GitHub deployment report with:
                              - Repository creation confirmation
                              - Repository URL
                              - Commit details
                              - Push confirmation
                              - DEPLOYMENT_REPORT.md file
                              - Verification that code is accessible on GitHub"""
      )