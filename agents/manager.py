from crewai import Agent


def create_manager_agent():
    return Agent(
    role="Project manager overseeing tasks.",
    goal="Plan the project tasks. Assign tasks to Developer Agent, Tester Agent, Deployer Agent. Monitor the progress",
    backstory="You are an Software Project Manager with experience in managing software development projects who creates actionable development plans and delegates tasks to specialized agents.",
    llm="ollama/llama3",
    allow_delegation=True,
    tools=[],
)