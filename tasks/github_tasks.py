"""GitHub Tasks - Split into repository creation and code deployment"""
from crewai import Task
from typing import Optional, List


def create_github_repository_task(
    agent,
    repo_name: str,
    description: str,
    github_username: str,
    local_path: str,  # Add this parameter
    visibility: str = "public",
    license_type: str = "MIT",
    context_tasks: Optional[List] = None
):
    """Task to create GitHub repository and clone it locally."""
    
    return Task(
        description=f"""Create a new GitHub repository and clone it to local directory for development.

REPOSITORY NAME: {repo_name}
GITHUB USERNAME: {github_username}
LOCAL PATH: {local_path}
DESCRIPTION: {description}
VISIBILITY: {visibility}
LICENSE: {license_type}

═══════════════════════════════════════════════════════════════════════════════
YOUR RESPONSIBILITIES:
═══════════════════════════════════════════════════════════════════════════════

STEP 1: CREATE GITHUB REPOSITORY
───────────────────────────────────────────────────────────────────────────────
□ Use Create GitHub repository tool
□ Repository settings:
  - Name: {repo_name}
  - Description: {description}
  - Visibility: {visibility}
  - Initialize: YES (with README) - THIS IS IMPORTANT FOR CLONING
  - Add .gitignore: NO (developer will create appropriate one)
  - License: {license_type}
  - Has issues: YES
  - Has wiki: NO
  - Has projects: NO

IMPORTANT: Initialize the repository with a README so it has an initial commit.
This makes cloning and pushing easier.

STEP 2: CLONE REPOSITORY LOCALLY
───────────────────────────────────────────────────────────────────────────────
□ Use Clone GitHub repository tool
□ Clone URL: https://github.com/{github_username}/{repo_name}.git
□ Local path: {local_path}
□ Branch: main
□ Verify clone was successful
□ Confirm local directory exists with README.md

═══════════════════════════════════════════════════════════════════════════════
TOOLS TO USE (IN ORDER):
═══════════════════════════════════════════════════════════════════════════════

1. Create GitHub repository - Create empty repo on GitHub
2. Clone GitHub repository - Clone repo to {local_path}
3. Get repository status - Verify everything is ready

═══════════════════════════════════════════════════════════════════════════════
SUCCESS CRITERIA:
═══════════════════════════════════════════════════════════════════════════════

Setup is successful when:
✅ Repository exists on GitHub: https://github.com/{github_username}/{repo_name}
✅ Repository cloned to: {local_path}
✅ Local .git directory exists
✅ README.md exists locally
✅ Git remote 'origin' configured
✅ Working tree is clean
✅ Ready for development team to write code

═══════════════════════════════════════════════════════════════════════════════
IMPORTANT NOTES:
═══════════════════════════════════════════════════════════════════════════════

⚠ The repository MUST be initialized with a README
⚠ Clone must succeed before proceeding
⚠ All subsequent work will happen in: {local_path}
⚠ Developer, Tester will work in the cloned directory
⚠ Final deployment will push from this local directory back to GitHub

This creates a proper git workflow:
1. Create remote repository (GitHub)
2. Clone to local (this task)
3. Develop locally (Developer agent)
4. Test locally (Tester agent)
5. Commit and push (Deployment agent)
""",
        
        agent=agent,
        context=context_tasks,
        expected_output="""Repository creation and clone report:

1. ✅ GitHub Repository Created
   - Name: {repo_name}
   - URL: https://github.com/{github_username}/{repo_name}
   - Clone URL: https://github.com/{github_username}/{repo_name}.git
   - Visibility: {visibility}
   - Status: Initialized with README

2. ✅ Repository Cloned Locally
   - Local path: {local_path}
   - Branch: main
   - Remote: origin → https://github.com/{github_username}/{repo_name}.git
   - Files: README.md, .git/

3. ✅ Git Status
   - Working tree: Clean
   - Branch: main
   - Tracking: origin/main
   - Ready for development

**Status**: ✅ REPOSITORY READY FOR DEVELOPMENT

**Next Steps**:
- Developer agent will write code in: {local_path}
- Tester agent will test code in: {local_path}
- Deployment agent will commit and push from: {local_path}

**Important**: All agents must work in {local_path} directory."""
    )


def create_github_deployment_task(
    agent,
    project_dir: str,
    repo_name: str,
    github_username: str,
    context_tasks: Optional[List] = None
):
    """Task to commit and push code to the already-cloned repository."""
    
    return Task(
        description=f"""Commit and push all developed and tested code to GitHub.

PROJECT DIRECTORY: {project_dir}
REPOSITORY: https://github.com/{github_username}/{repo_name}

═══════════════════════════════════════════════════════════════════════════════
⚠️ CRITICAL: USE EXACT TOOL NAMES - DO NOT MAKE UP TOOL NAMES
═══════════════════════════════════════════════════════════════════════════════

You MUST use these EXACT tool names (copy-paste them):
1. "Get repository status"
2. "List directory contents"
3. "Read file content"
4. "Write content to a file"
5. "Add and commit changes"
6. "Push to remote repository"
7. "Create and push tag"

DO NOT create variations like:
❌ "Initialize the Git repository for committing changes"
❌ "Commit the changes"
❌ "Push code to GitHub"

Use ONLY the exact names listed above!

═══════════════════════════════════════════════════════════════════════════════
IMPORTANT CONTEXT:
═══════════════════════════════════════════════════════════════════════════════

The repository has already been:
✅ Created on GitHub
✅ Cloned to {project_dir}
✅ Set up with git remote

Your job is to:
1. Verify all files from development and testing
2. Create/update documentation files
3. Commit everything
4. Push to GitHub

═══════════════════════════════════════════════════════════════════════════════
DEPLOYMENT WORKFLOW:
═══════════════════════════════════════════════════════════════════════════════

📋 PHASE 1: PRE-COMMIT VERIFICATION
───────────────────────────────────────────────────────────────────────────────

1. Verify git repository status:
   □ Use get_repo_status tool
   □ Confirm we're in a git repository
   □ Confirm remote 'origin' exists
   □ Note current branch (should be 'main')

2. Check all required files exist:
   □ Use list_directory tool
   □ Verify: Source code, tests, documentation
   □ Check for .gitignore (should exist from developer)
   □ Check for README.md
   □ Verify no sensitive data (.env with secrets, API keys)

3. Enhance/Create documentation:
   □ Update README.md if needed (make it comprehensive)
   □ Create CHANGELOG.md with v1.0.0 entry
   □ Verify LICENSE file exists
   □ Add any missing documentation

📦 PHASE 2: COMMIT ALL CHANGES
───────────────────────────────────────────────────────────────────────────────

1. Stage all files:
   □ Use commit_changes tool with add_all=True
   □ This will stage all new and modified files
   □ .gitignore will prevent unwanted files

2. Create commit:
   □ Commit message: "Complete project implementation with tests and documentation"
   □ Include bullet points about what's included
   □ Use commit_changes tool

3. Verify commit:
   □ Use get_repo_status tool
   □ Confirm commit was created
   □ Confirm working tree is clean

🚀 PHASE 3: PUSH TO GITHUB
───────────────────────────────────────────────────────────────────────────────

1. Push code:
   □ Use push_to_remote tool
   □ Remote: origin
   □ Branch: main
   □ This pushes to: https://github.com/{github_username}/{repo_name}

2. Create version tag:
   □ Use create_tag tool
   □ Tag: v1.0.0
   □ Message: "Initial release - fully functional project"
   □ Push tag: YES

✅ PHASE 4: VERIFICATION
───────────────────────────────────────────────────────────────────────────────

1. Final checks:
   □ Use get_repo_status tool
   □ Confirm working tree is clean
   □ Confirm all commits pushed
   □ Confirm no uncommitted changes

2. Create deployment report:
   □ Use write_file tool
   □ File: {project_dir}/DEPLOYMENT_REPORT.md
   □ Include: All deployment details, URLs, file counts, git operations

═══════════════════════════════════════════════════════════════════════════════
TOOLS TO USE (IN ORDER):
═══════════════════════════════════════════════════════════════════════════════

1. get_repo_status - Check current git status
2. list_directory - Verify all files
3. read_file - Check existing documentation
4. write_file - Create/update docs and DEPLOYMENT_REPORT.md
5. commit_changes - Commit all changes (add_all=True)
6. push_to_remote - Push to origin/main
7. create_tag - Create and push v1.0.0 tag
8. get_repo_status - Final verification

═══════════════════════════════════════════════════════════════════════════════
CRITICAL REQUIREMENTS:
═══════════════════════════════════════════════════════════════════════════════

YOU MUST:
✅ Verify .gitignore exists and works
✅ Check NO sensitive data in files (.env, secrets, keys)
✅ Commit ALL source code, tests, docs
✅ Push to existing remote (already configured)
✅ Create v1.0.0 tag
✅ Create DEPLOYMENT_REPORT.md
✅ Verify push succeeded

YOU MUST NEVER:
❌ Commit .env files with real secrets
❌ Commit node_modules/, __pycache__/, build/
❌ Force push (--force) without good reason
❌ Skip verification steps

═══════════════════════════════════════════════════════════════════════════════
SUCCESS CRITERIA:
═══════════════════════════════════════════════════════════════════════════════

Deployment succeeds when:
✅ All code committed to git
✅ All changes pushed to GitHub
✅ Tag v1.0.0 exists on GitHub
✅ Repository accessible: https://github.com/{github_username}/{repo_name}
✅ README displays correctly on GitHub
✅ No sensitive data exposed
✅ DEPLOYMENT_REPORT.md created
✅ Working tree clean

═══════════════════════════════════════════════════════════════════════════════
BEGIN DEPLOYMENT!
═══════════════════════════════════════════════════════════════════════════════
""",
        
        agent=agent,
        context=context_tasks,
        expected_output="""Deployment completion report:

1. ✅ Pre-Deployment Verification
   - Git repository status: Clean
   - All source files present
   - Documentation complete
   - No sensitive data found

2. ✅ Git Operations
   - All files staged
   - Commit created: [hash]
   - Pushed to: origin/main
   - Tag v1.0.0 created and pushed

3. ✅ Deployment Verification
   - Working tree: Clean
   - All changes on GitHub
   - Repository URL: https://github.com/{github_username}/{repo_name}
   - Tag visible on GitHub

4. ✅ Documentation
   - DEPLOYMENT_REPORT.md created
   - Complete deployment details recorded

**Status**: ✅ DEPLOYMENT SUCCESSFUL  
**Repository**: https://github.com/{github_username}/{repo_name}  
**Ready for**: Production use"""
    )