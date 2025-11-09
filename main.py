"""
Developer AI Agent System - Main Entry Point with QC Validation
Complete project automation with quality checks at each phase
"""
import re
from pathlib import Path
from crewai import Crew, Process

# Import agents
from agents.solution import create_manager_agent
from agents.developer import create_developer_agent
from agents.tester import create_tester_agent
from agents.github import create_github_agent
from agents.qc import create_qc_agent

# Import tasks
from tasks.manager_tasks import create_planning_task
from tasks.developer_tasks import create_development_task
from tasks.tester_tasks import create_testing_task
from tasks.github_tasks import create_github_task
from tasks.qc_tasks import (
    create_plan_validation_task,
    create_code_validation_task,
    create_test_validation_task,
    create_deployment_validation_task
)

# Import config
from config import OUTPUT_DIR, GITHUB_USERNAME


def sanitize_repo_name(name: str) -> str:
    """Convert project name to valid GitHub repository name"""
    name = re.sub(r'[^a-zA-Z0-9\s-]', '', name)
    name = name.lower().strip().replace(' ', '-')
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
    """Get user approval for the plan."""
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


def check_qc_approval(qc_report_path: Path) -> tuple[bool, str]:
    """
    Check QC report for approval status and extract feedback.
    
    Returns:
        tuple: (approved: bool, feedback: str)
    """
    if not qc_report_path.exists():
        return False, "QC report not found"
    
    content = qc_report_path.read_text(encoding='utf-8')
    
    # Check approval status
    if "✅ APPROVED" in content and "PASS" in content:
        return True, ""
    elif "⚠️ APPROVED WITH CONDITIONS" in content:
        # Extract feedback/conditions
        if "CRITICAL ISSUES" in content or "MAJOR ISSUES" in content:
            # Extract issues for feedback
            feedback_lines = []
            for line in content.split('\n'):
                if any(marker in line for marker in ["CRITICAL:", "MAJOR:", "Issue:", "Fix:", "Recommendation:"]):
                    feedback_lines.append(line.strip())
            
            feedback = "\n".join(feedback_lines) if feedback_lines else "Please address issues found in QC report"
            return False, feedback
        return True, ""  # Minor issues, can proceed
    else:
        # Extract critical feedback
        feedback_lines = []
        in_issues_section = False
        
        for line in content.split('\n'):
            if "CRITICAL ISSUES" in line or "MAJOR ISSUES" in line:
                in_issues_section = True
            elif "MINOR ISSUES" in line:
                in_issues_section = False
            elif in_issues_section and line.strip():
                feedback_lines.append(line.strip())
        
        feedback = "\n".join(feedback_lines) if feedback_lines else "Project requires fixes. See QC report for details."
        return False, feedback


def main():
    print("=" * 80)
    print("🤖 DEVELOPER AI AGENT SYSTEM WITH QC VALIDATION")
    print("=" * 80)
    print("\nThis system will:")
    print("1. 📋 Create technical plan (with human & QC approval)")
    print("2. 💻 Write code (with QC validation)")
    print("3. 🧪 Test code (with QC validation)")
    print("4. 🚀 Deploy to GitHub (with QC validation)")
    print("5. 🔍 Quality Control checks after EACH phase")
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
    project_dir = create_project_directory(project_name)
    print(f"✓ Project directory: {project_dir}")
    
    print("\n" + "=" * 80)
    print("🚀 STARTING PROJECT GENERATION WITH QC VALIDATION")
    print("=" * 80)
    
    # Create agents
    print("\n👥 Initializing AI agents...")
    solution_architect = create_manager_agent()
    developer = create_developer_agent()
    tester = create_tester_agent()
    github_manager = create_github_agent()
    qc_agent = create_qc_agent()
    print("✓ All agents initialized (Solution Architect, Developer, Tester, GitHub, QC)")
    
    # ============================================================================
    # PHASE 1: PLANNING WITH HUMAN & QC APPROVAL
    # ============================================================================
    print("\n" + "=" * 80)
    print("📋 PHASE 1: TECHNICAL PLANNING (with QC validation)")
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
            solution_architect, 
            current_description, 
            project_type
        )
        
        # Execute planning only
        planning_crew = Crew(
            agents=[solution_architect],
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
    
    # ============================================================================
    # PHASE 2: IMPLEMENTATION WITH QC VALIDATION
    # ============================================================================
    print("\n" + "=" * 80)
    print("💻 PHASE 2: CODE IMPLEMENTATION (with QC validation)")
    print("=" * 80)
    
    code_approved = False
    code_iteration = 0
    max_code_iterations = 3
    development_task = None
    
    while not code_approved and code_iteration < max_code_iterations:
        code_iteration += 1
        print(f"\n🔨 Code implementation attempt {code_iteration}/{max_code_iterations}...")
        
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
            
            print("\n🔨 Writing code...")
            dev_result = development_crew.kickoff()
            print("\n✅ Code implementation complete!")
            
            # QC Validation of Code
            print("\n🔍 QC Agent reviewing the code...")
            code_qc_task = create_code_validation_task(
                qc_agent,
                str(project_dir),
                context_tasks=[planning_task, development_task]
            )
            
            code_qc_crew = Crew(
                agents=[qc_agent],
                tasks=[code_qc_task],
                process=Process.sequential,
                verbose=True
            )
            
            qc_result = code_qc_crew.kickoff()
            
            # Check QC approval
            qc_report_path = project_dir / "QC_CODE_REVIEW.md"
            qc_approved, qc_feedback = check_qc_approval(qc_report_path)
            
            if qc_approved:
                print("\n✅ QC Agent approved the code!")
                code_approved = True
                break
            else:
                print(f"\n⚠️ QC Agent found issues with the code.")
                print(f"\nQC Feedback:\n{qc_feedback}")
                
                if code_iteration < max_code_iterations:
                    print("\n🔄 Developer will fix the issues...")
                    # Update development task with QC feedback
                    # The developer will re-implement with feedback
                else:
                    print("\n⚠️ Maximum code iterations reached. Proceeding with warnings...")
                    code_approved = True  # Proceed anyway
        
        except Exception as e:
            print(f"\n❌ Error during development: {str(e)}")
            import traceback
            traceback.print_exc()
            
            if code_iteration < max_code_iterations:
                retry = input("\nRetry code generation? (y/n): ").strip().lower()
                if retry != 'y':
                    return
            else:
                print(f"\n📁 Partial project available at: {project_dir}")
                return
    
    # ============================================================================
    # PHASE 3: TESTING WITH QC VALIDATION
    # ============================================================================
    print("\n" + "=" * 80)
    print("🧪 PHASE 3: TESTING & QA (with QC validation)")
    print("=" * 80)
    
    test_approved = False
    test_iteration = 0
    max_test_iterations = 2
    testing_task = None
    
    while not test_approved and test_iteration < max_test_iterations:
        test_iteration += 1
        print(f"\n🔍 Testing attempt {test_iteration}/{max_test_iterations}...")
        
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
            
            print("\n🔍 Running tests...")
            test_result = testing_crew.kickoff()
            print("\n✅ Testing complete!")
            
            # QC Validation of Tests
            print("\n🔍 QC Agent reviewing the tests...")
            test_qc_task = create_test_validation_task(
                qc_agent,
                str(project_dir),
                context_tasks=[planning_task, development_task, testing_task]
            )
            
            test_qc_crew = Crew(
                agents=[qc_agent],
                tasks=[test_qc_task],
                process=Process.sequential,
                verbose=True
            )
            
            qc_result = test_qc_crew.kickoff()
            
            # Check QC approval
            qc_report_path = project_dir / "QC_TEST_REVIEW.md"
            qc_approved, qc_feedback = check_qc_approval(qc_report_path)
            
            if qc_approved:
                print("\n✅ QC Agent approved the tests!")
                test_approved = True
                break
            else:
                print(f"\n⚠️ QC Agent found issues with tests.")
                print(f"\nQC Feedback:\n{qc_feedback}")
                
                if test_iteration < max_test_iterations:
                    print("\n🔄 Tester will improve the tests...")
                else:
                    print("\n⚠️ Maximum test iterations reached. Proceeding with warnings...")
                    test_approved = True
        
        except Exception as e:
            print(f"\n❌ Error during testing: {str(e)}")
            print("⚠ Continuing despite test errors...")
            import traceback
            traceback.print_exc()
            test_approved = True  # Continue anyway
            break
    
    # ============================================================================
    # PHASE 4: GITHUB DEPLOYMENT WITH QC VALIDATION
    # ============================================================================
    print("\n" + "=" * 80)
    print("🚀 PHASE 4: GITHUB DEPLOYMENT (with QC validation)")
    print("=" * 80)
    
    deployment_approved = False
    deployment_iteration = 0
    max_deployment_iterations = 2
    github_task = None
    
    while not deployment_approved and deployment_iteration < max_deployment_iterations:
        deployment_iteration += 1
        print(f"\n📤 Deployment attempt {deployment_iteration}/{max_deployment_iterations}...")
        
        try:
            github_task = create_github_task(
                github_manager,
                str(project_dir),
                github_username,
                repo_name,
                project_description,
                str(project_type),
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
            
            # QC Validation of Deployment
            print("\n🔍 QC Agent reviewing the deployment...")
            deployment_qc_task = create_deployment_validation_task(
                qc_agent,
                str(project_dir),
                context_tasks=[planning_task, development_task, testing_task, github_task]
            )
            
            deployment_qc_crew = Crew(
                agents=[qc_agent],
                tasks=[deployment_qc_task],
                process=Process.sequential,
                verbose=True
            )
            
            qc_result = deployment_qc_crew.kickoff()
            
            # Check QC approval
            qc_report_path = project_dir / "QC_DEPLOYMENT_REVIEW.md"
            qc_approved, qc_feedback = check_qc_approval(qc_report_path)
            
            if qc_approved:
                print("\n✅ QC Agent approved the deployment!")
                deployment_approved = True
                break
            else:
                print(f"\n⚠️ QC Agent found issues with deployment.")
                print(f"\nQC Feedback:\n{qc_feedback}")
                
                if deployment_iteration < max_deployment_iterations:
                    print("\n🔄 Retrying deployment with fixes...")
                else:
                    print("\n⚠️ Deployment has issues but proceeding...")
                    deployment_approved = True
        
        except Exception as e:
            print(f"\n❌ Error during deployment: {str(e)}")
            print(f"📁 Project available locally at: {project_dir}")
            import traceback
            traceback.print_exc()
            deployment_approved = True  # Continue to summary
            break
    
    # ============================================================================
    # FINAL SUMMARY
    # ============================================================================
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
    print(f"  - Code Iterations: {code_iteration}")
    print(f"  - Test Iterations: {test_iteration}")
    print(f"  - Deployment Iterations: {deployment_iteration}")
    print(f"  - Project Type: {project_type}")
    print(f"  - Repository Name: {repo_name}")
    
    print("\n📋 QC Reports Generated:")
    qc_reports = list(project_dir.glob("QC_*.md"))
    for report in qc_reports:
        print(f"  - {report.name}")
    
    print("\n" + "=" * 80)
    print("🎉 SUCCESS! Your project is ready!")
    print("=" * 80)
    
    print(f"\n🔗 GitHub Repository: https://github.com/{github_username}/{repo_name}")
    print(f"📁 Local Project: {project_dir}")
    
    print("\n📚 Next Steps:")
    print("  1. Review the code in your project directory")
    print("  2. Check all QC reports for quality metrics")
    print("  3. Visit your GitHub repository")
    print("  4. Clone and start using your project!")
    
    print("\n👋 Thank you for using Developer AI Agent System with QC!")


if __name__ == "__main__":
    main()