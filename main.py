"""
Developer AI Agent System - Main Entry Point
Complete project automation: Plan -> Code -> Test -> Deploy to GitHub
"""
import os
import re
from pathlib import Path
from datetime import datetime
from crewai import Crew, Process

# Import agents
from agents.manager import create_manager_agent
from agents.developer import create_developer_agent
from agents.tester import create_tester_agent
from agents.github import create_github_agent

# Import tasks
from tasks.manager_tasks import create_planning_task
from tasks.developer_tasks import create_development_task
from tasks.tester_tasks import create_testing_task
from tasks.github_tasks import create_github_task

# Import config
from config import OUTPUT_DIR, MAX_ITERATIONS


def sanitize_repo_name(name: str) -> str:
    """Convert project name to valid GitHub repository name"""
    # Remove special characters, convert to lowercase, replace spaces with hyphens
    name = re.sub(r'[^a-zA-Z0-9\s-]', '', name)
    name = name.lower().strip().replace(' ', '-')
    # Remove consecutive hyphens
    name = re.sub(r'-+', '-', name)
    return name


def create_project_directory(project_name: str) -> Path:
    """Create and return project directory path"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = sanitize_repo_name(project_name)
    project_dir = OUTPUT_DIR / f"{safe_name}_{timestamp}"
    project_dir.mkdir(parents=True, exist_ok=True)
    return project_dir


def main():
    print("=" * 80)
    print("🤖 DEVELOPER AI AGENT SYSTEM")
    print("=" * 80)
    print("\nThis system will:")
    print("1. 📋 Analyze your project requirements and create a technical plan")
    print("2. 💻 Write complete, working code")
    print("3. 🧪 Test and validate the code")
    print("4. 🚀 Deploy to GitHub repository")
    print("\n" + "=" * 80)
    
    # Get user input
    print("\n📝 PROJECT DETAILS")
    print("-" * 80)
    project_description = input("\nDescribe your project (be detailed): ").strip()
    
    if not project_description:
        print("❌ Project description cannot be empty!")
        return
    
    project_type = input("\nProject type (python/web/ml/javascript) [python]: ").strip() or "python"
    project_name = input("\nProject name (for GitHub repo): ").strip()
    
    if not project_name:
        project_name = "ai-generated-project"
    
    # Sanitize repository name
    repo_name = sanitize_repo_name(project_name)
    print(f"\n✓ Repository name will be: {repo_name}")
    
    # Create project directory
    project_dir = create_project_directory(project_name)
    print(f"✓ Project directory: {project_dir}")
    
    # Optional: GitHub deployment
    deploy_to_github = input("\nDeploy to GitHub? (yes/no) [yes]: ").strip().lower()
    deploy_to_github = deploy_to_github in ['yes', 'y', '']
    
    print("\n" + "=" * 80)
    print("🚀 STARTING PROJECT GENERATION")
    print("=" * 80)
    
    # Create agents
    print("\n👥 Initializing AI agents...")
    manager = create_manager_agent()
    developer = create_developer_agent()
    tester = create_tester_agent()
    github_manager = create_github_agent() if deploy_to_github else None
    
    # Create tasks
    print("📋 Creating task pipeline...")
    planning_task = create_planning_task(manager, project_description, project_type)
    development_task = create_development_task(
        developer, 
        str(project_dir),
        context_tasks=[planning_task]
    )
    testing_task = create_testing_task(
        tester,
        str(project_dir),
        context_tasks=[planning_task, development_task]
    )
    
    tasks = [planning_task, development_task, testing_task]
    agents = [manager, developer, tester]
    
    if deploy_to_github:
        github_task = create_github_task(
            github_manager,
            str(project_dir),
            repo_name,
            project_description,
            context_tasks=[planning_task, development_task, testing_task]
        )
        tasks.append(github_task)
        agents.append(github_manager)
    
    # Create and run crew
    print("\n🎯 Assembling crew...")
    crew = Crew(
        agents=agents,
        tasks=tasks,
        process=Process.sequential,
        verbose=True,
        max_rpm=10
    )
    
    print("\n" + "=" * 80)
    print("⚡ EXECUTING PROJECT WORKFLOW")
    print("=" * 80)
    print("\nThis may take several minutes depending on project complexity...")
    print("The agents are working on your project...\n")
    
    try:
        # Execute the crew
        result = crew.kickoff()
        
        print("\n" + "=" * 80)
        print("✅ PROJECT GENERATION COMPLETE!")
        print("=" * 80)
        
        print(f"\n📁 Project Location: {project_dir}")
        print(f"\n📄 Files Generated:")
        for file in project_dir.rglob("*"):
            if file.is_file():
                print(f"  - {file.relative_to(project_dir)}")
        
        print(f"\n📊 Final Report:")
        print("-" * 80)
        print(result)
        
        print("\n" + "=" * 80)
        print("🎉 SUCCESS! Your project is ready!")
        print("=" * 80)
        
        if deploy_to_github:
            print(f"\n🔗 Check your GitHub repository: https://github.com/YOUR_USERNAME/{repo_name}")
        
    except Exception as e:
        print(f"\n❌ Error during execution: {str(e)}")
        print(f"\n📁 Partial project may be available at: {project_dir}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()