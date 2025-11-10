from crewai import Task


def create_planning_task(agent, project_dir: str, project_description: str, project_type: str = "python"):
    return Task(
        description=f"""As the Senior Solution Architect, create a COMPREHENSIVE and DETAILED technical specification 
                        for the following project. Your specification must be complete enough that a developer can implement it WITHOUT 
                        asking any clarification questions.

                        ╔═══════════════════════════════════════════════════════════════╗
                        ║                    PROJECT REQUIREMENTS                        ║
                        ╚═══════════════════════════════════════════════════════════════╝
                        PROJECT DIRECTORY: {project_dir} (Note: always follow this location)
                        PROJECT DESCRIPTION:
                        {project_description}

                        PROJECT TYPE: {project_type}

                        ╔═══════════════════════════════════════════════════════════════╗
                        ║                  YOUR DELIVERABLES (MANDATORY)                 ║
                        ╚═══════════════════════════════════════════════════════════════╝

                        You MUST provide ALL of the following sections in your technical plan:

                        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        1. PROJECT OVERVIEW & OBJECTIVES
                        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        □ Problem Statement: What specific problem does this solve?
                        □ Target Users: Who will use this?
                        □ Core Functionality: What are the 3-5 main features?
                        □ Success Criteria: How do we know it works?
                        □ Scope: What's IN scope and OUT of scope?

                        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        2. TECHNOLOGY STACK (Specific Versions Required)
                        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        □ Programming Language: [name] [version] - Why chosen?
                        □ Core Framework: [name==version] - Why chosen?
                        □ Key Libraries: List each with version and purpose
                        Example: 
                        - requests==2.31.0 # For HTTP requests
                        - pandas==2.1.0 # For data manipulation
                        - etc.
                        □ Database/Storage: [type] [version] if needed
                        □ External Services/APIs: List any third-party integrations
                        □ Development Tools: Testing framework, linter, formatter

                        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        3. COMPLETE FILE & DIRECTORY STRUCTURE
                        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        Provide EXACT file structure with descriptions:

                        For Example (ADJUST AS NEEDED):
                        ```
                        project_name/
                        ├── src/
                        │   ├── __init__.py              # Package initialization
                        │   ├── main.py                  # Entry point - handles CLI/startup
                        │   ├── core/
                        │   │   ├── __init__.py
                        │   │   ├── engine.py            # Core business logic
                        │   │   └── models.py            # Data models and classes
                        │   ├── utils/
                        │   │   ├── __init__.py
                        │   │   ├── helpers.py           # Utility functions
                        │   │   └── validators.py        # Input validation
                        │   └── config/
                        │       ├── __init__.py
                        │       └── settings.py          # Configuration management
                        ├── tests/
                        │   ├── __init__.py
                        │   ├── test_core.py             # Tests for core functionality
                        │   └── test_utils.py            # Tests for utilities
                        ├── data/                        # Sample data or storage
                        ├── docs/                        # Documentation
                        ├── requirements.txt             # Python dependencies
                        ├── README.md                    # Project documentation
                        ├── .env.example                 # Environment variables template
                        ├── .gitignore                   # Git ignore rules
                        └── setup.py or pyproject.toml   # Package configuration
                        ```

                        □ Explain WHY each directory/file exists
                        □ Specify which files are auto-generated vs manually created

                        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        4. DATA MODELS & SCHEMAS (If Applicable)
                        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        For EACH data model:
                        □ Class/Table name
                        □ All fields with types and constraints
                        □ Relationships to other models
                        □ Default values
                        □ Validation rules

                        Example:
                        ```python
                        class User:
                            id: int (primary key, auto-increment)
                            username: str (unique, max_length=50, required)
                            email: str (unique, email format, required)
                            created_at: datetime (auto, default=now)
                            is_active: bool (default=True)
                        ```

                        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        5. MODULE SPECIFICATIONS (For Each File)
                        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        For EACH module/file:
                        □ Module Purpose: Single sentence description
                        □ Public Functions/Classes:
                        - Function signature with type hints
                        - Parameters with descriptions
                        - Return type and description
                        - Example usage
                        □ Private Functions: Internal helpers
                        □ Dependencies: What it imports from other modules
                        □ Error Handling: What exceptions it raises

                        Example:
                        ```python
                        # file: src/core/engine.py
                        # Purpose: Main processing engine for data transformation

                        def process_data(input_data: List[Dict], config: Config) -> ProcessedResult:
                            '''
                            Process input data according to configuration
                            
                            Args:
                                input_data: List of dictionaries with keys: ['id', 'value', 'timestamp']
                                config: Configuration object with processing parameters
                                
                            Returns:
                                ProcessedResult object with processed data and statistics
                                
                            Raises:
                                ValueError: If input_data is empty or invalid format
                                ConfigError: If config is missing required fields
                                
                            Example:
                                >>> data = [{{\'id\': 1, \'value\': 100}}]
                                >>> result = process_data(data, config)
                                >>> print(result.total_processed)
                            '''
                        ```

                        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        6. API DESIGN (If Applicable)
                        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        For web services/APIs:
                        □ Base URL structure
                        □ All endpoints with:
                        - HTTP method (GET/POST/PUT/DELETE)
                        - Path with parameters
                        - Request body format (with example JSON)
                        - Response format (with example JSON)
                        - Status codes (200, 400, 404, etc.)
                        - Authentication requirements

                        Example:
                        ```
                        POST /api/users
                        Request: {{"username": "john", "email": "john@example.com"}}
                        Response: {{"id": 1, "username": "john", "created": "2024-01-01"}}
                        Status: 201 Created
                        Auth: Bearer token required
                        ```

                        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        7. DETAILED IMPLEMENTATION STEPS
                        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        Provide SEQUENTIAL, NUMBERED steps:

                        Step 1: Project Setup
                        - Create directory structure (specify exact commands)
                        - Initialize virtual environment
                        - Create requirements.txt with dependencies

                        Step 2: Configuration Setup
                        - Create config/settings.py
                        - Implement configuration loading
                        - Add environment variable support

                        Step 3: Data Models Implementation
                        - Create models.py
                        - Implement User class with all fields
                        - Add validation methods

                        [Continue with ALL steps needed...]

                        Each step should:
                        □ Be specific about which file to create/modify
                        □ Specify what code to write (high-level but clear)
                        □ Indicate dependencies on previous steps
                        □ Include validation checkpoints

                        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        8. ERROR HANDLING STRATEGY
                        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        □ Exception Hierarchy: Custom exceptions to create
                        □ Input Validation: Where and how to validate
                        □ Error Messages: User-friendly messages
                        □ Logging Strategy: What to log and where
                        □ Recovery Mechanisms: How to handle failures

                        Example:
                        ```python
                        class ValidationError(Exception):
                            pass

                        def validate_input(data):
                            if not data:
                                raise ValidationError("Input cannot be empty")
                            # etc.
                        ```

                        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        9. TESTING STRATEGY
                        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        □ Test Framework: pytest, unittest, etc.
                        □ Test Coverage Target: Aim for X% coverage
                        □ Unit Tests:
                        - List specific functions to test
                        - Key test cases for each
                        - Edge cases to cover
                        □ Integration Tests: System-level test scenarios
                        □ Test Fixtures: What test data is needed
                        □ Mocking Strategy: What to mock and why

                        Example Test Cases:
                        ```
                        test_process_data_valid_input()
                        test_process_data_empty_input_raises_error()
                        test_process_data_invalid_format_raises_error()
                        test_process_data_with_config()
                        ```

                        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        10. CONFIGURATION & ENVIRONMENT (If Applicable)
                        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        □ Environment Variables: List all with descriptions
                        □ Configuration Files: Format and structure
                        □ Default Values: What are the defaults?
                        □ Secrets Management: How to handle sensitive data

                        Example .env:
                        ```
                        DATABASE_URL=sqlite:///app.db
                        API_KEY=your_api_key_here
                        DEBUG=False
                        LOG_LEVEL=INFO
                        ```

                        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        11. USAGE EXAMPLES & DOCUMENTATION
                        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        □ Installation Steps: Exact commands
                        □ Basic Usage Example: Code snippet
                        □ Advanced Usage: More complex scenarios
                        □ CLI Commands: If applicable
                        □ Expected Output: What users should see

                        Example:
                        ```bash
                        # Installation
                        git clone <repo>
                        cd project
                        python -m venv venv
                        source venv/bin/activate
                        pip install -r requirements.txt

                        # Basic Usage
                        python main.py --input data.csv --output results.json

                        # Expected Output
                        Processing 100 records...
                        ✓ Complete! Results saved to results.json
                        ```

                        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        12. EDGE CASES & CONSIDERATIONS
                        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                        □ Known Limitations: What it can't do
                        □ Performance Considerations: Expected bottlenecks
                        □ Security Considerations: Potential vulnerabilities
                        □ Scalability: How to handle growth
                        □ Edge Cases: Unusual scenarios to handle

                        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

                        ╔═══════════════════════════════════════════════════════════════╗
                        ║                    QUALITY CHECKLIST                           ║
                        ╚═══════════════════════════════════════════════════════════════╝

                        Before submitting your plan, verify:
                        ☑ All file names are EXACT (not "handler.py" but "user_handler.py")
                        ☑ All library versions are SPECIFIED (not "requests" but "requests==2.31.0")
                        ☑ All function signatures have TYPE HINTS
                        ☑ All modules have clear PURPOSE statements
                        ☑ Implementation steps are NUMBERED and SEQUENTIAL
                        ☑ Error handling is SPECIFIED for each critical function
                        ☑ Test cases are CONCRETE (not "test the function" but "test_function_with_empty_input")
                        ☑ Configuration is COMPLETE with examples
                        ☑ Documentation includes WORKING examples
                        ☑ No vague terms like "implement business logic" or "add error handling"

                        ╔═══════════════════════════════════════════════════════════════╗
                        ║                      REMEMBER                                  ║
                        ╚═══════════════════════════════════════════════════════════════╝

                        A developer reading your plan should be able to:
                        1. Understand EXACTLY what to build
                        2. Know EXACTLY which files to create
                        3. Know EXACTLY what code goes in each file
                        4. Implement WITHOUT asking clarification questions

                        BE SPECIFIC. BE DETAILED. BE COMPLETE.""",
        
        agent=agent,
        expected_output="""A comprehensive technical specification document (3000+ words) containing:

                            ✓ Complete project overview with clear objectives
                            ✓ Technology stack with specific versions and justifications
                            ✓ Detailed file structure with purpose of each file
                            ✓ Complete data models with all fields and types (if applicable)
                            ✓ Module specifications with function signatures
                            ✓ API design with request/response examples (if applicable)
                            ✓ Sequential implementation steps (20+ steps)
                            ✓ Error handling strategy with examples
                            ✓ Comprehensive testing strategy with specific test cases
                            ✓ Configuration requirements with examples
                            ✓ Working usage examples with expected output
                            ✓ Edge cases and considerations

                            The specification must be detailed enough that any competent developer can implement 
                            the project exactly as specified without requiring clarification."""
    )