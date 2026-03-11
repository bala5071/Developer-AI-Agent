# Developer AI Agent 🤖💻

## 📖 Overview
Developer AI Agent is a multi-agent system built to automate the software development lifecycle. By orchestrating specialized AI agents—an Architect, a Developer, and a Tester—it translates natural language ideas into fully tested, executable code. 

Built with **Python**, **OpenAI API**, and **CrewAI**, this project goes beyond simple prompt wrapping by implementing **iterative feedback loops** and **function calling**. If the Tester agent identifies a bug, the code is autonomously routed back to the Developer for refinement before the final output is presented, ensuring reliability and an autonomous development process.

## 🏗️ Architecture

The system utilizes CrewAI to coordinate the following autonomous agents:

1. **The Architect:** Analyzes the natural language prompt, determines the optimal tech stack, and designs the software structure.
2. **The Developer:** Writes the actual code based on the Architect's blueprint.
3. **The Tester:** Evaluates the generated code, looks for syntax error and provides specific feedback to the Developer if errors are found.
4. **The GitHub:** Creates and commits the generated code into the GitHub Repository after user approval.


## Check out the project WebCalculator (https://github.com/bala5071/webcalculator), which was created by this multi-agentic system
