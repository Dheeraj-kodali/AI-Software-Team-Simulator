from agents.pm_agent import pm_agent
from agents.architect_agent import architect_agent
from agents.database_agent import database_agent
from agents.backend_agent import backend_agent

project = "Hospital Management System"

pm_output = pm_agent(project)

arch_output = architect_agent(
    project,
    pm_output
)

db_output = database_agent(
    project,
    arch_output
)

backend_output = backend_agent(
    project,
    arch_output,
    db_output
)

print(backend_output)