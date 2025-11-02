# """GitHub Deployment Tasks"""
# from crewai import Task


# def create_github_task(agent, project_dir: str, github_username: str, repo_name: str, 
#                        description: str, context_tasks: list = None):
#     return Task(
#         description=f"""Deploy the project to GitHub:

#                         PROJECT DIRECTORY: {project_dir}
#                         GITHUB USERNAME: {github_username}
#                         REPOSITORY NAME: {repo_name}
#                         DESCRIPTION: {description}

#                         Your responsibilities:
#                         1. Create a comprehensive .gitignore file
#                         2. Create/update README.md with:
#                            - Project badges (if applicable)
#                            - Clear installation instructions
#                            - Usage examples
#                            - Features list
#                            - License information
#                         3. Initialize Git repository
#                         4. Create initial commit with message: "Initial commit: {description}"
#                         5. Create GitHub repository
#                         6. Push all code to GitHub
#                         7. Verify the repository is accessible
#                         8. Create a DEPLOYMENT_REPORT.md with:
#                            - Repository URL
#                            - Deployment steps taken
#                            - Any issues encountered
#                            - Instructions for cloning and running

#                         IMPORTANT:
#                         - Use GitHub Full Deploy tool for complete workflow
#                         - Ensure all files are committed
#                         - Verify the push was successful
#                         - Make sure README.md is comprehensive

#                         Make the repository professional and ready for public viewing.""",
#          agent=agent,
#          context=context_tasks,
#          expected_output="""GitHub deployment report with:
#                               - Repository creation confirmation
#                               - Repository URL
#                               - Commit details
#                               - Push confirmation
#                               - DEPLOYMENT_REPORT.md file
#                               - Verification that code is accessible on GitHub"""
#       )

from crewai import Task
from typing import Optional, List


def create_github_task(
    agent,
    project_dir: str,
    repo_name: str,
    description: str,
    github_username: str,
    project_type: str = "general",  # web_app, mobile_app, cli_tool, library, api_service, desktop_app
    tech_stack: str = "Python",  # Python, JavaScript, Java, Go, Rust, C#, etc.
    deployment_target: str = "GitHub",  # GitHub, GitLab, Bitbucket, Azure DevOps
    license_type: str = "MIT",  # MIT, Apache-2.0, GPL-3.0, BSD-3-Clause, Proprietary
    visibility: str = "public",  # public or private
    context_tasks: Optional[List] = None
):
    
    task_description = f"""Deploy the project to version control and prepare for distribution:

PROJECT DIRECTORY: {project_dir}
PROJECT TYPE: {project_type}
TECHNOLOGY STACK: {tech_stack}
DEPLOYMENT TARGET: {deployment_target}
REPOSITORY NAME: {repo_name}
GITHUB USERNAME/ORGANIZATION: {github_username}
PROJECT DESCRIPTION: {description}
LICENSE: {license_type}
VISIBILITY: {visibility}

═══════════════════════════════════════════════════════════════════════════════
YOUR DEPLOYMENT & DISTRIBUTION RESPONSIBILITIES:
═══════════════════════════════════════════════════════════════════════════════

📋 PHASE 1: PRE-DEPLOYMENT PREPARATION
───────────────────────────────────────────────────────────────────────────────
1. Create comprehensive .gitignore file for {tech_stack}:
   - Exclude build artifacts, dependencies, cache files
   - Exclude environment files (.env, *.local)
   - Exclude sensitive data (secrets/, credentials/, *.key)
   - Exclude IDE/editor files (.vscode/, .idea/, *.swp)
   - Exclude logs and temporary files
   - Include language-specific exclusions for {tech_stack}
   - Verify critical files (source code, docs, configs) are NOT ignored

📚 PHASE 2: COMPREHENSIVE README ENHANCEMENT
───────────────────────────────────────────────────────────────────────────────
2. Create/enhance README.md with professional documentation:
   
   REQUIRED SECTIONS:
   A. Header with project title and badges:
      - Language/framework badge
      - License badge
      - Build status (if CI configured)
      - Version badge
      - Platform badge (if applicable)
   
   B. Project description:
      - One-line tagline
      - Detailed explanation (2-3 paragraphs)
      - Problem it solves
      - Target audience
      - Key differentiators
   
   C. Table of Contents (for longer READMEs)
   
   D. Features section:
      - List all major features with emojis
      - Highlight unique capabilities
   
   E. Demo section (if applicable):
      - Screenshots, GIFs, or video links
      - Live demo URL
   
   F. Technology Stack:
      - Core technologies with versions
      - Key libraries/dependencies
      - Development tools
      - Infrastructure (if applicable)
   
   G. Prerequisites:
      - Required software/tools with versions
      - Platform requirements (OS, memory, storage)
      - Optional dependencies
   
   H. Installation Instructions:
      - Quick install (if package available)
      - From source (step-by-step):
        * Clone repository
        * Install dependencies (language-specific commands)
        * Build instructions (if needed)
      - Platform-specific steps (Windows, macOS, Linux)
   
   I. Configuration:
      - Environment variables setup
      - Configuration file examples
      - Database setup (if applicable)
      - API keys and credentials (templates only!)
   
   J. Usage:
      - Quick start guide
      - Basic examples with code blocks
      - Advanced examples
      - CLI usage (if CLI tool)
      - API usage (if library/API)
      - Expected output examples
   
   K. API Reference (if applicable):
      - Class/function documentation
      - Parameters and return values
      - Code examples
      - REST endpoints (if API service)
   
   L. Examples:
      - Multiple use case demonstrations
      - Reference to examples/ directory
   
   M. Testing:
      - How to run tests
      - Test structure explanation
      - Coverage information
   
   N. Deployment:
      - Docker instructions
      - Cloud platform deployment
      - Manual deployment steps
   
   O. Architecture (for complex projects):
      - System architecture diagram/description
      - Project structure
      - Design decisions
   
   P. Roadmap (optional):
      - Completed features
      - In-progress features
      - Planned features
   
   Q. Troubleshooting:
      - Common issues and solutions
      - How to get help
   
   R. Contributing:
      - Contribution guidelines
      - How to submit PRs
      - Code style guide reference
   
   S. License:
      - License type ({license_type})
      - Link to LICENSE file
      - Third-party licenses
   
   T. Acknowledgments:
      - Credits and attributions
      - Built with section
   
   U. Contact & Support:
      - Author information
      - Project links
      - Support channels

🔧 PHASE 3: ADDITIONAL REPOSITORY FILES
───────────────────────────────────────────────────────────────────────────────
3. Create essential repository files:
   
   A. LICENSE file:
      - Create {license_type} license file
      - Include copyright year and owner
   
   B. CONTRIBUTING.md (for public projects):
      - Code of conduct
      - How to contribute
      - Style guides
      - Development setup
      - Testing guidelines
   
   C. CHANGELOG.md:
      - Version history structure
      - Initial release entry
   
   D. CODE_OF_CONDUCT.md (for public projects):
      - Community guidelines
      - Reporting process
   
   E. SECURITY.md (if applicable):
      - Supported versions
      - Security reporting process
   
   F. Issue Templates (.github/ISSUE_TEMPLATE/ or .gitlab/):
      - Bug report template
      - Feature request template
      - Question template
   
   G. Pull Request Template:
      - PR description template
      - Checklist for contributors
   
   H. CI/CD Workflows (based on {deployment_target}):
      - Continuous integration (build, test, lint)
      - Automated releases
      - Deployment workflow
      - Security scanning

📦 PHASE 4: REPOSITORY INITIALIZATION
───────────────────────────────────────────────────────────────────────────────
4. Initialize and prepare Git repository:
   
   A. Initialize Git:
      ```bash
      cd {project_dir}
      git init
      ```
   
   B. Configure Git:
      ```bash
      git config user.name "Author Name"
      git config user.email "author@email.com"
      ```
   
   C. Stage all files:
      ```bash
      git add .
      ```
      
      VERIFY STAGING:
      ✅ Ensure these ARE staged:
      - All source code files
      - README.md, LICENSE, CONTRIBUTING.md
      - .gitignore
      - Configuration templates (.env.example)
      - Documentation files
      - Test files
      - Build configurations
      - CI/CD workflows
      
      ❌ Ensure these are NOT staged:
      - .env files (secrets)
      - node_modules/, __pycache__/, vendor/
      - Build artifacts (dist/, build/, target/)
      - IDE files (.vscode/, .idea/)
      - Log files
      - Any credentials or sensitive data
   
   D. Create initial commit:
      ```bash
      git commit -m "Initial commit: {description}
      
      - Set up {tech_stack} project structure
      - Add core {project_type} functionality
      - Include comprehensive documentation
      - Configure build and test systems
      - Add CI/CD workflows
      - Add {license_type} license"
      ```

🚀 PHASE 5: REMOTE REPOSITORY CREATION & PUSH
───────────────────────────────────────────────────────────────────────────────
5. Create and push to remote repository:
   
   A. Create remote repository on {deployment_target}:
      
      For GitHub:
      ```bash
      gh repo create {github_username}/{repo_name} \\
        --{visibility} \\
        --description "{description}" \\
        --source . \\
        --push
      ```
      
      Or via web interface:
      - Name: {repo_name}
      - Description: {description}
      - Visibility: {visibility}
      - Initialize: No (already initialized)
      
      For GitLab:
      - Use GitLab API or web interface
      - Set project visibility
      - Configure project settings
      
      For Bitbucket:
      - Use Bitbucket API or web interface
      - Set repository type
      - Configure access settings
      
      For Azure DevOps:
      - Use Azure CLI or web interface
      - Set project visibility
      - Configure repository policies
   
   B. Add remote origin:
      ```bash
      git remote add origin <repository-url>
      ```
   
   C. Push code to remote:
      ```bash
      git branch -M main
      git push -u origin main
      ```
   
   D. Create and push tags (for releases):
      ```bash
      git tag -a v1.0.0 -m "Release version 1.0.0"
      git push origin v1.0.0
      ```

🔍 PHASE 6: REPOSITORY CONFIGURATION
───────────────────────────────────────────────────────────────────────────────
6. Configure repository settings:
   
   A. General Settings:
      - Set repository description
      - Add topics/tags for discoverability:
        * Language: {tech_stack.lower()}
        * Type: {project_type.replace('_', '-')}
        * Relevant framework/library tags
      - Set website URL (if applicable)
      - Configure default branch (main)
   
   B. Access & Permissions:
      - Set visibility ({visibility})
      - Configure collaborator access (if applicable)
      - Set up team permissions (if organization)
   
   C. Branch Protection Rules:
      - Protect main branch
      - Require pull request reviews
      - Require status checks to pass
      - Require conversation resolution
   
   D. Platform-Specific Features:
      
      GitHub:
      - Enable Issues
      - Enable Discussions (for community projects)
      - Enable Projects (if using boards)
      - Configure GitHub Pages (if docs site)
      - Enable Dependabot alerts
      - Enable security advisories
      - Configure code scanning
      
      GitLab:
      - Enable merge requests
      - Configure CI/CD settings
      - Set up runners
      - Configure container registry
      
      Bitbucket:
      - Enable pull requests
      - Configure pipelines
      - Set up branch permissions
      
      Azure DevOps:
      - Configure build pipelines
      - Set up release pipelines
      - Configure boards
   
   E. Repository Labels (GitHub/GitLab):
      - bug, enhancement, documentation
      - good first issue, help wanted
      - question, wontfix, duplicate

✅ PHASE 7: POST-DEPLOYMENT VERIFICATION
───────────────────────────────────────────────────────────────────────────────
7. Verify repository accessibility and completeness:
   
   A. Repository Checks:
      ✓ Repository URL is accessible
      ✓ README displays correctly with formatting
      ✓ All badges are working
      ✓ Code is properly syntax-highlighted
      ✓ Directory structure is clear
      ✓ Documentation is readable
      ✓ Links in README are not broken
      ✓ Images/GIFs load correctly (if applicable)
      ✓ License file is present and correct
      ✓ .gitignore is working properly
      ✓ No sensitive data is exposed
   
   B. Clone and Run Test:
      ```bash
      # Clone in a temporary directory
      cd /tmp
      git clone <repository-url>
      cd {repo_name}
      
      # Follow installation instructions from README
      [installation commands]
      
      # Run tests (if applicable)
      [test commands]
      
      # Run application
      [run commands]
      ```
      
      VERIFY:
      ✓ Clone works without errors
      ✓ Installation steps are accurate
      ✓ Dependencies install correctly
      ✓ Tests pass (if included)
      ✓ Application runs successfully
      ✓ Documentation matches actual behavior
   
   C. CI/CD Verification (if configured):
      ✓ Trigger workflow manually or via commit
      ✓ Verify builds succeed
      ✓ Check test execution
      ✓ Verify deployment (if automated)
      ✓ Review workflow logs

📊 PHASE 8: DEPLOYMENT REPORT GENERATION
───────────────────────────────────────────────────────────────────────────────
8. Create comprehensive DEPLOYMENT_REPORT.md:

```markdown
# Deployment Report - {repo_name}

**Date:** [Current Date and Time]
**Deployed By:** Deployment Agent
**Target Platform:** {deployment_target}
**Project Type:** {project_type}
**Technology Stack:** {tech_stack}
**Visibility:** {visibility}

---

## 📋 Executive Summary

✅ **Deployment Status:** SUCCESSFUL / PARTIAL / FAILED
✅ **Repository:** <repository-url>
✅ **Clone URL (HTTPS):** <https-clone-url>
✅ **Clone URL (SSH):** <ssh-clone-url>

---

## 🎯 Repository Information

**Repository Details:**
- **Name:** {repo_name}
- **Description:** {description}
- **Owner:** {github_username}
- **License:** {license_type}
- **Primary Language:** {tech_stack}
- **Project Type:** {project_type}
- **Visibility:** {visibility}

**Repository URLs:**
- **Main Repository:** <main-url>
- **Issues:** <issues-url>
- **Pull Requests:** <pr-url>
- **Wiki:** <wiki-url> (if enabled)
- **Documentation:** <docs-url> (if applicable)

**Topics/Tags:**
[List of topics/tags added]

---

## 📦 Deployment Steps Completed

### Phase 1: Pre-Deployment Preparation
- ✅ Created comprehensive .gitignore for {tech_stack}
- ✅ Verified sensitive files are excluded
- ✅ Confirmed source code files are included

### Phase 2: Documentation
- ✅ Created/enhanced README.md with all required sections
- ✅ Added project badges and shields
- ✅ Included installation instructions for all platforms
- ✅ Added usage examples and code snippets
- ✅ Documented all features
- ✅ Added troubleshooting section

### Phase 3: Repository Files
- ✅ Created LICENSE file ({license_type})
- ✅ Created CONTRIBUTING.md (if public)
- ✅ Created CHANGELOG.md
- ✅ Created CODE_OF_CONDUCT.md (if public)
- ✅ Created SECURITY.md (if applicable)
- ✅ Added issue templates
- ✅ Added pull request template
- ✅ Configured CI/CD workflows

### Phase 4: Repository Initialization
- ✅ Initialized Git repository
- ✅ Configured Git user settings
- ✅ Staged all appropriate files
- ✅ Verified .gitignore is working
- ✅ Created initial commit

**Initial Commit Details:**
- **Message:** "Initial commit: {description}"
- **Files Committed:** [Number] files
- **Commit Hash:** [hash]

### Phase 5: Remote Repository & Push
- ✅ Created remote repository on {deployment_target}
- ✅ Added remote origin
- ✅ Pushed main branch
- ✅ Created and pushed v1.0.0 tag
- ✅ Verified push success

**Push Details:**
- **Branch:** main
- **Commits Pushed:** 1
- **Files Uploaded:** [Number] files
- **Repository Size:** [Size]

### Phase 6: Repository Configuration
- ✅ Set repository description
- ✅ Added topics/tags for discoverability
- ✅ Configured branch protection rules
- ✅ Enabled issues and discussions
- ✅ Configured security features
- ✅ Set up repository labels

### Phase 7: Post-Deployment Verification
- ✅ Verified repository accessibility
- ✅ Confirmed README renders correctly
- ✅ Tested clone operation
- ✅ Verified installation instructions
- ✅ Confirmed no sensitive data exposed
- ✅ Tested CI/CD workflows (if configured)

---

## 🔍 Repository Contents

**Project Structure:**
```
{repo_name}/
├── Source Files: [Count] files
├── Test Files: [Count] files
├── Documentation: [Count] files
├── Configuration Files: [Count] files
└── Total Files: [Count] files
```

**Key Files Deployed:**
- ✅ README.md (comprehensive documentation)
- ✅ LICENSE ({license_type})
- ✅ .gitignore ({tech_stack}-specific)
- ✅ CONTRIBUTING.md
- ✅ CHANGELOG.md
- ✅ Source code files
- ✅ Test files
- ✅ Configuration files
- ✅ CI/CD workflows

---

## 🛠️ Repository Features Enabled

**Version Control Features:**
- ✅ Git repository initialized
- ✅ Branch: main (default)
- ✅ Protected branches configured
- ✅ Version tags enabled

**Collaboration Features:**
- ✅ Issues enabled
- ✅ Pull requests enabled
- ✅ Discussions enabled (if public)
- ✅ Wiki enabled (if configured)
- ✅ Projects enabled (if configured)

**Automation Features:**
- ✅ CI/CD workflows configured
- ✅ Automated testing (if configured)
- ✅ Automated releases (if configured)
- ✅ Dependabot alerts enabled
- ✅ Security scanning enabled

**Documentation Features:**
- ✅ Comprehensive README
- ✅ Contributing guidelines
- ✅ Code of conduct
- ✅ License information
- ✅ Issue templates
- ✅ PR templates

---

## ⚠️ Issues Encountered

### Critical Issues
[None / List any critical issues]

### Minor Issues
[None / List any minor issues]

### Warnings
[None / List any warnings]

---

## 📝 Verification Results

### Clone Test
```bash
$ git clone <repository-url>
Status: ✅ SUCCESS / ❌ FAILED
Time: [Duration]
```

### Installation Test
```bash
$ cd {repo_name}
$ [installation commands]
Status: ✅ SUCCESS / ❌ FAILED
```

### Run Test
```bash
$ [run commands]
Status: ✅ SUCCESS / ❌ FAILED
Output: [Brief output description]
```

### CI/CD Test (if applicable)
```
Workflow: [Workflow name]
Status: ✅ PASSED / ❌ FAILED
Duration: [Duration]
```

---

## 🚀 Getting Started

### For Users

**Clone the Repository:**
```bash
# HTTPS
git clone <https-clone-url>

# SSH
git clone <ssh-clone-url>
```

**Install Dependencies:**
```bash
cd {repo_name}
[installation commands based on {tech_stack}]
```

**Run the Application:**
```bash
[run commands]
```

### For Contributors

**Fork and Clone:**
```bash
# Fork on {deployment_target}
# Clone your fork
git clone <your-fork-url>
cd {repo_name}
```

**Create Feature Branch:**
```bash
git checkout -b feature/your-feature-name
```

**Install Development Dependencies:**
```bash
[dev installation commands]
```

**Make Changes and Test:**
```bash
[test commands]
```

**Submit Pull Request:**
```bash
git push origin feature/your-feature-name
# Create PR on {deployment_target}
```

---

## 📚 Additional Resources

**Documentation:**
- README: <readme-url>
- Contributing Guidelines: <contributing-url>
- Code of Conduct: <code-of-conduct-url>
- License: <license-url>

**Support:**
- Issues: <issues-url>
- Discussions: <discussions-url>
- Documentation: <docs-url> (if applicable)

**Project Links:**
- Repository: <main-url>
- Website: <website-url> (if applicable)
- Demo: <demo-url> (if applicable)

---

## ✅ Deployment Checklist

### Pre-Deployment
- [x] Code is tested and working
- [x] Documentation is complete
- [x] License is chosen and added
- [x] .gitignore is configured
- [x] Sensitive data is excluded

### Deployment
- [x] Git repository initialized
- [x] Remote repository created
- [x] Code pushed successfully
- [x] Tags created
- [x] Repository configured

### Post-Deployment
- [x] Repository is accessible
- [x] README displays correctly
- [x] Clone and install work
- [x] No sensitive data exposed
- [x] CI/CD works (if configured)

---

## 🎯 Next Steps

### Immediate Actions
1. ✅ Repository is live and accessible
2. ✅ Share repository URL with stakeholders
3. ✅ Announce release (if public)

### Recommended Actions
1. Star the repository (if on GitHub)
2. Watch for issues and pull requests
3. Set up project board (if needed)
4. Configure GitHub Pages (if docs site)
5. Add more examples and tutorials
6. Engage with community

### Future Enhancements
1. Add more comprehensive tests
2. Improve documentation with videos/GIFs
3. Create additional examples
4. Set up automated releases
5. Configure code coverage reporting
6. Add performance benchmarks

---

## 📊 Deployment Statistics

**Deployment Time:** [Duration]
**Files Deployed:** [Count]
**Lines of Code:** [Count] (approx)
**Repository Size:** [Size]
**Contributors:** 1 (initial)

---

## 🏆 Deployment Success Criteria

- ✅ Repository created successfully
- ✅ All files committed and pushed
- ✅ README is comprehensive and accurate
- ✅ Documentation is complete
- ✅ Clone and installation work
- ✅ No sensitive data exposed
- ✅ Repository is properly configured
- ✅ CI/CD workflows operational (if configured)

**Overall Deployment Status: ✅ SUCCESSFUL**

---

## 📞 Support & Contact

For issues, questions, or contributions:
- **Repository:** <repository-url>
- **Issues:** <issues-url>
- **Owner:** {github_username}

---

<p align="center">
  <strong>Repository deployed successfully! 🎉</strong>
</p>
<p align="center">
  Deployed on: [Date and Time]
</p>
```

═══════════════════════════════════════════════════════════════════════════════
TOOLS TO USE:
═══════════════════════════════════════════════════════════════════════════════

Required Tools:
□ File Writer: Create/update .gitignore, README.md, LICENSE, etc.
□ File Reader: Read existing files to enhance them
□ Directory Lister: Verify project structure
□ Git Command Executor: Initialize repo, commit, push
□ {deployment_target} API Tool: Create repository, configure settings
□ Verification Tool: Test clone and installation

═══════════════════════════════════════════════════════════════════════════════
CRITICAL REQUIREMENTS:
═══════════════════════════════════════════════════════════════════════════════

YOU MUST:
✅ Use {deployment_target} deployment tool for complete workflow
✅ Create comprehensive .gitignore for {tech_stack}
✅ Ensure README.md is professional and complete
✅ Verify no sensitive data (API keys, passwords, .env) is committed
✅ Test that repository is accessible
✅ Verify clone and installation work
✅ Create detailed DEPLOYMENT_REPORT.md
✅ Configure repository settings appropriately
✅ Add relevant topics/tags for discoverability
✅ Ensure all documentation is accurate

YOU MUST NEVER:
❌ Commit .env files or secrets
❌ Include API keys or credentials
❌ Push binary files or large datasets
❌ Leave placeholder text in README
❌ Skip verification steps
❌ Create incomplete documentation
❌ Ignore .gitignore configuration
❌ Push without testing locally
❌ Leave TODO comments in deployed code
❌ Expose sensitive information

═══════════════════════════════════════════════════════════════════════════════
SUCCESS CRITERIA:
═══════════════════════════════════════════════════════════════════════════════

Deployment is considered SUCCESSFUL when:
✅ Repository is created on {deployment_target}
✅ All code is pushed without errors
✅ README.md is comprehensive and renders correctly
✅ .gitignore excludes appropriate files
✅ No sensitive data is exposed
✅ Repository is accessible via URL
✅ Clone operation works correctly
✅ Installation instructions are accurate
✅ DEPLOYMENT_REPORT.md is complete
✅ Repository is configured properly
✅ CI/CD workflows pass (if configured)

═══════════════════════════════════════════════════════════════════════════════
BEGIN PROFESSIONAL DEPLOYMENT NOW!
═══════════════════════════════════════════════════════════════════════════════
"""

    expected_output = f"""{deployment_target} deployment report with:

REQUIRED DELIVERABLES:
1. ✅ Repository Creation Confirmation
   - Repository URL
   - Clone URLs (HTTPS and SSH)
   - Repository settings confirmation

2. ✅ Files Deployed
   - Complete .gitignore for {tech_stack}
   - Enhanced README.md with all sections
   - LICENSE file ({license_type})
   - CONTRIBUTING.md (if public)
   - CHANGELOG.md
   - CODE_OF_CONDUCT.md (if public)
   - SECURITY.md (if applicable)
   - Issue and PR templates
   - CI/CD workflow files

3. ✅ Git Operations
   - Repository initialized
   - Initial commit details (hash, message, files)
   - Remote added
   - Push confirmation
   - Tags created (v1.0.0)

4. ✅ Repository Configuration
   - Description set
   - Topics/tags added
   - Branch protection configured
   - Features enabled (issues, discussions, etc.)
   - Security features enabled

5. ✅ Verification Results
   - Repository accessibility confirmed
   - Clone test passed
   - Installation test passed
   - README renders correctly
   - No sensitive data exposed
   - CI/CD workflows pass (if configured)

6. ✅ DEPLOYMENT_REPORT.md
   - Comprehensive deployment report
   - All phases documented
   - Verification results included
   - Getting started instructions
   - Next steps and recommendations
   - Deployment statistics

7. ✅ Quality Assurance
   - Professional README with all sections
   - Complete documentation
   - Proper .gitignore configuration
   - No placeholders or TODOs
   - Repository ready for public viewing

FINAL VERIFICATION:
- Repository URL is accessible: <url>
- Clone works: git clone <url>
- Installation works: Tested and confirmed
- Documentation is complete: All sections present
- No sensitive data exposed: Verified
- Repository is professional: Ready for users/contributors

DEPLOYMENT STATUS: ✅ SUCCESSFUL

Repository is live at: <repository-url>
Ready for users, contributors, and production use!"""

    return Task(
        description=task_description,
        agent=agent,
        context=context_tasks,
        expected_output=expected_output
    )