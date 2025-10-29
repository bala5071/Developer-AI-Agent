from crewai import Crew, Task, LLM
from agents.manager import create_manager_agent
from agents.developer import create_developer_agent
from agents.tester import create_tester_agent
from agents.deployer import create_deployer_agent


def main():
    user_prompt = input("Describe your project idea:\n> ")

    manager_agent = create_manager_agent()
    developer_agent = create_developer_agent()
    tester_agent = create_tester_agent()
    deployer_agent = create_deployer_agent()

    plan_task = Task(
        description=f"Plan how to build the project: '{user_prompt}'. "
                    "Output architecture, file structure, and steps.",
        agent=manager_agent,
        expected_output="A structured project plan in JSON format"
    )

    code_task = Task(
        description="Generate the full project code based on the plan.",
        agent=developer_agent,
        expected_output="A set of files saved to ./workspace/"
    )

    test_task = Task(
        description="Test the generated project and fix issues if any.",
        agent=tester_agent,
        expected_output="Report on successful execution or error logs"
    )

    deploy_task = Task(
        description="Deploy or run the project locally, and summarize results.",
        agent=deployer_agent,
        expected_output="Local deployment instructions or running server output"
    )


    crew = Crew(
        agents=[manager_agent, developer_agent, tester_agent, deployer_agent],
        tasks=[plan_task, code_task, test_task, deploy_task],
        verbose=True
    )

    result = crew.kickoff()
    print("\n=== Final Output ===\n", result)

if __name__ == "__main__":
    main()
