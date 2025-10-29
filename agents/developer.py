from crewai import Agent


def create_developer_agent():
    return Agent(
    role="Software developer responsible for coding tasks.",
    goal="Write clean and efficient code. Modify the code based on the project plan. Implement features as per specifications. Fix bugs and issues.",
    backstory="You are a skilled full stack software developer with experience in various programming languages and frameworks, responsible for turning project requirements into functional software.",
    llm="ollama/codellama",
    allow_delegation=True,
    tools=[],
)