from crewai import Agent
from config import AGENT_VERBOSE


def create_manager_agent():
    return Agent(
    role="Project manager and Architect",
    goal="Analyze project requirements and create comprehensive technical plans.",
    backstory="""You are an expert software architect with 15+ years of experience.
        You excel at breaking down complex problems into manageable components,
        selecting appropriate technologies, and designing scalable solutions.
        You consider best practices, security, performance, and maintainability.""",
    llm="ollama/llama3",
    verbose=AGENT_VERBOSE,
    allow_delegation=False,
    max_iter=15
)