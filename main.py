import re
from pathlib import Path
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
from tasks.github_tasks import create_github_deployment_task, create_github_repository_task

# Import config
from config import OUTPUT_DIR, GITHUB_USERNAME


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
    safe_name = sanitize_repo_name(project_name)
    project_dir = OUTPUT_DIR / f"{safe_name}"
    project_dir.mkdir(parents=True, exist_ok=True)
    return project_dir


def display_plan(plan: str) -> None:
    """Display the technical plan in a formatted way"""
    print("\n" + "=" * 80)
    print("📋 TECHNICAL PLAN")
    print("=" * 80)
    print(plan)
    print("=" * 80)


def get_user_approval() -> tuple[bool, str]:
    """
    Get user approval for the plan.
    
    Returns:
        tuple: (approved: bool, feedback: str)
    """
    print("\n" + "=" * 80)
    print("👤 HUMAN REVIEW REQUIRED")
    print("=" * 80)
    print("\nPlease review the technical plan above.")
    print("\nOptions:")
    print("  1. Approve - Proceed with implementation")
    print("  2. Request Changes - Provide additional requirements")
    print("  3. Cancel - Exit the system")
    
    while True:
        choice = input("\nYour choice (1/2/3): ").strip()
        
        if choice == "1":
            print("\n✓ Plan approved! Proceeding with implementation...")
            return True, ""
        
        elif choice == "2":
            print("\n📝 Please provide your additional requirements or changes:")
            print("(You can provide multiple lines. Press Enter twice to finish)\n")
            
            feedback_lines = []
            empty_count = 0
            
            while empty_count < 2:
                line = input()
                if line.strip():
                    feedback_lines.append(line)
                    empty_count = 0
                else:
                    empty_count += 1
            
            feedback = "\n".join(feedback_lines).strip()
            
            if feedback:
                print(f"\n✓ Feedback received ({len(feedback)} characters)")
                return False, feedback
            else:
                print("\n⚠ No feedback provided. Please try again.")
                continue
        
        elif choice == "3":
            print("\n❌ Project generation cancelled by user.")
            return False, "CANCELLED"
        
        else:
            print("\n⚠ Invalid choice. Please enter 1, 2, or 3.")


def main():
    print("=" * 80)
    print("🤖 DEVELOPER AI AGENT SYSTEM")
    print("=" * 80)
    print("\nThis system will:")
    print("1. 📋 Analyze your project requirements and create a technical plan")
    print("2. 👤 Get your approval (you can request changes)")
    print("3. 💻 Write complete, working code")
    print("4. 🧪 Test and validate the code")
    print("5. 🚀 Deploy to GitHub repository")
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

    github_username = GITHUB_USERNAME
    
    # Sanitize repository name
    repo_name = sanitize_repo_name(project_name)
    print(f"\n✓ Repository name will be: {repo_name}")
    
    # Create project directory
    project_dir = OUTPUT_DIR / f"{repo_name}"
    print(f"✓ Project will be cloned to: {project_dir}")
    
    print("\n" + "=" * 80)
    print("🚀 STARTING PROJECT GENERATION")
    print("=" * 80)
    
    # Create agents
    print("\n👥 Initializing AI agents...")
    manager = create_manager_agent()
    developer = create_developer_agent()
    tester = create_tester_agent()
    github_manager = create_github_agent()

    print("\n" + "=" * 80)
    print("🔧 PHASE 0: GITHUB REPOSITORY CREATION")
    print("=" * 80)
    
    try:
        print("\n📦 Creating GitHub repository...")
        
        repo_creation_task = create_github_repository_task(
            github_manager,
            repo_name,
            project_description,
            github_username,
            str(project_dir),
            visibility="public",
            license_type="MIT"
        )
        
        repo_creation_crew = Crew(
            agents=[github_manager],
            tasks=[repo_creation_task],
            process=Process.sequential,
            verbose=True
        )
        
        repo_result = repo_creation_crew.kickoff()
        print("\n✅ GitHub repository created and ready!")
        print(f"📍 Repository will be at: https://github.com/{github_username}/{repo_name}")
        
    except Exception as e:
        print(f"\n❌ Error creating repository: {str(e)}")
        print("Project generation cannot continue without repository.")
        return
    
    # PHASE 1: PLANNING WITH HUMAN APPROVAL LOOP
    print("\n" + "=" * 80)
    print("📋 PHASE 1: TECHNICAL PLANNING")
    print("=" * 80)
    
    plan_approved = False
    iteration_count = 0
    max_iterations = 5
    current_description = project_description
    
    while not plan_approved and iteration_count < max_iterations:
        iteration_count += 1
        print(f"\n🔄 Planning iteration {iteration_count}/{max_iterations}...")
        
        # Create planning task
        planning_task = create_planning_task(
            manager, 
            str(project_dir),
            current_description, 
            project_type
        )
        
        # Execute planning only
        planning_crew = Crew(
            agents=[manager],
            tasks=[planning_task],
            process=Process.sequential,
            verbose=True
        )
        
        try:
            # Get the plan
            plan_result = planning_crew.kickoff()
            
            # Display the plan
            display_plan(str(plan_result))
            
            # Save plan to file for reference
            plan_file = project_dir / "TECHNICAL_PLAN.md"
            plan_file.write_text(str(plan_result), encoding='utf-8')
            print(f"\n💾 Plan saved to: {plan_file}")
            
            # Get user approval
            approved, feedback = get_user_approval()
            
            if feedback == "CANCELLED":
                print("\n👋 Goodbye!")
                return
            
            if approved:
                plan_approved = True
                print("\n✅ Plan approved! Moving to implementation phase...")
                break
            else:
                # User requested changes
                print("\n🔄 Incorporating your feedback into the plan...")
                current_description = f"""{current_description}

ADDITIONAL REQUIREMENTS FROM USER (Iteration {iteration_count}):
{feedback}

Please update the technical plan to incorporate these new requirements."""
                
                print("\n📝 Updated requirements received. Regenerating plan...")
        
        except Exception as e:
            print(f"\n❌ Error during planning: {str(e)}")
            retry = input("\nWould you like to retry? (y/n): ").strip().lower()
            if retry != 'y':
                return
            continue
    
    if not plan_approved:
        print(f"\n⚠ Maximum planning iterations ({max_iterations}) reached.")
        print("Please refine your requirements and try again.")
        return
    
    # PHASE 2: IMPLEMENTATION
    print("\n" + "=" * 80)
    print("💻 PHASE 2: CODE IMPLEMENTATION")
    print("=" * 80)
    
    try:
        development_task = create_development_task(
            developer, 
            str(project_dir),
            str(project_type),
            context_tasks=[planning_task]
        )
        
        development_crew = Crew(
            agents=[developer],
            tasks=[development_task],
            process=Process.sequential,
            verbose=True
        )
        
        print("\n🔨 Writing code... This may take several minutes...")
        dev_result = development_crew.kickoff()
        print("\n✅ Code implementation complete!")
        
    except Exception as e:
        print(f"\n❌ Error during development: {str(e)}")
        print(f"📁 Partial project available at: {project_dir}")
        import traceback
        traceback.print_exc()
        return
    
    # PHASE 3: TESTING
    print("\n" + "=" * 80)
    print("🧪 PHASE 3: TESTING & QUALITY ASSURANCE")
    print("=" * 80)
    
    try:
        testing_task = create_testing_task(
            tester,
            str(project_dir),
            str(project_type),
            context_tasks=[planning_task, development_task]
        )
        
        testing_crew = Crew(
            agents=[tester],
            tasks=[testing_task],
            process=Process.sequential,
            verbose=True
        )
        
        print("\n🔍 Running tests and quality checks...")
        test_result = testing_crew.kickoff()
        print("\n✅ Testing complete!")
        
        # Display test report if exists
        test_report = project_dir / "TEST_REPORT.md"
        if test_report.exists():
            print(f"\n📊 Test report saved to: {test_report}")
        
    except Exception as e:
        print(f"\n❌ Error during testing: {str(e)}")
        print("⚠ Continuing to deployment despite test errors...")
        import traceback
        traceback.print_exc()
    
    # PHASE 4: GITHUB DEPLOYMENT
    print("\n" + "=" * 80)
    print("🚀 PHASE 4: GITHUB DEPLOYMENT")
    print("=" * 80)
    
    try:
        github_task = create_github_deployment_task(
            agent=github_manager,
            project_dir=str(project_dir),
            repo_name=repo_name,
            github_username=github_username,
            context_tasks=[planning_task, development_task, testing_task]
        )
        
        github_crew = Crew(
            agents=[github_manager],
            tasks=[github_task],
            process=Process.sequential,
            verbose=True
        )
        
        print("\n📤 Deploying to GitHub...")
        github_result = github_crew.kickoff()
        print("\n✅ GitHub deployment complete!")
        
    except Exception as e:
        print(f"\n❌ Error during GitHub deployment: {str(e)}")
        print(f"📁 Project available locally at: {project_dir}")
        import traceback
        traceback.print_exc()
    
    # FINAL SUMMARY
    print("\n" + "=" * 80)
    print("✅ PROJECT GENERATION COMPLETE!")
    print("=" * 80)
    
    print(f"\n📁 Project Location: {project_dir}")
    print(f"\n📄 Files Generated:")
    file_count = 0
    for file in sorted(project_dir.rglob("*")):
        if file.is_file():
            file_count += 1
            print(f"  {file_count}. {file.relative_to(project_dir)}")
    
    print(f"\n📊 Project Summary:")
    print(f"  - Total Files: {file_count}")
    print(f"  - Planning Iterations: {iteration_count}")
    print(f"  - Project Type: {project_type}")
    print(f"  - Repository Name: {repo_name}")
    
    print("\n" + "=" * 80)
    print("🎉 SUCCESS! Your project is ready!")
    print("=" * 80)
    
    print(f"\n🔗 GitHub Repository: https://github.com/{github_username}/{repo_name}")
    print(f"📁 Local Project: {project_dir}")
    
    print("\n📚 Next Steps:")
    print("  1. Review the code in your project directory")
    print("  2. Check the TEST_REPORT.md for quality metrics")
    print("  3. Visit your GitHub repository")
    print("  4. Clone and start using your project!")
    
    print("\n👋 Thank you for using Developer AI Agent System!")


if __name__ == "__main__":
    main()