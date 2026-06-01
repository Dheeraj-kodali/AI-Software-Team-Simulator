from agents.pm_agent import pm_agent
from agents.architect_agent import architect_agent

project = "Hospital Management System"

pm_output = pm_agent(project)

result = architect_agent(
    project,
    pm_output
)

print(result)