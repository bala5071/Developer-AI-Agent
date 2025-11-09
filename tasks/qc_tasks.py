"""Quality Control Tasks - Phase-specific validations"""
from crewai import Task


def create_plan_validation_task(agent, project_dir: str, context_tasks: list = None):
    """QC validation task for technical plan."""
    
    return Task(
        description=f"""Review the technical plan created by the Solution Architect.

PROJECT DIRECTORY: {project_dir}

Read the TECHNICAL_PLAN.md file and validate:

□ All required sections present
□ Technology stack appropriate
□ File structure complete
□ Implementation steps clear
□ No vague requirements
□ Error handling planned
□ Testing strategy defined

Create QC_PLAN_REVIEW.md with your findings.""",
        
        agent=agent,
        context=context_tasks,
        expected_output="""QC_PLAN_REVIEW.md with plan validation results"""
    )


def create_code_validation_task(agent, project_dir: str, context_tasks: list = None):
    """QC validation task for code implementation."""
    
    return Task(
        description=f"""Review the code created by the Developer.

PROJECT DIRECTORY: {project_dir}

Validate:
□ All planned files created
□ Syntax valid (use validate_syntax tool)
□ Code quality good (use lint_code tool)
□ Documentation present
□ No TODOs or placeholders
□ Error handling implemented
□ Security best practices followed

Create QC_CODE_REVIEW.md with your findings.""",
        
        agent=agent,
        context=context_tasks,
        expected_output="""QC_CODE_REVIEW.md with code validation results"""
    )


def create_test_validation_task(agent, project_dir: str, context_tasks: list = None):
    """QC validation task for tests."""
    
    return Task(
        description=f"""Review the tests created by the Tester.

PROJECT DIRECTORY: {project_dir}

Validate:
□ Test files exist
□ All tests pass
□ Coverage ≥ 80%
□ Edge cases tested
□ Test quality good

Read TEST_REPORT.md and create QC_TEST_REVIEW.md.""",
        
        agent=agent,
        context=context_tasks,
        expected_output="""QC_TEST_REVIEW.md with test validation results"""
    )


def create_deployment_validation_task(agent, project_dir: str, context_tasks: list = None):
    """QC validation task for GitHub deployment."""
    
    return Task(
        description=f"""Review the GitHub deployment.

PROJECT DIRECTORY: {project_dir}

Validate:
□ Repository created
□ Files committed
□ .gitignore appropriate
□ No sensitive data exposed
□ README comprehensive

Read DEPLOYMENT_REPORT.md and create QC_DEPLOYMENT_REVIEW.md.""",
        
        agent=agent,
        context=context_tasks,
        expected_output="""QC_DEPLOYMENT_REVIEW.md with deployment validation results"""
    )