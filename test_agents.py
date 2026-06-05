from agents.pm_agent import pm_agent
from agents.architect_agent import architect_agent
from agents.database_agent import database_agent
from agents.backend_agent import backend_agent
from agents.qa_agent import qa_agent
from agents.devops_agent import devops_agent
from agents.risk_agent import risk_agent
from agents.cost_agent import cost_agent
from agents.docs_agent import docs_agent

project = "Hospital Management System"

print("Testing PM...")
pm = pm_agent(project)

print("Testing Architect...")
arch = architect_agent(project, pm)

print("Testing Database...")
db = database_agent(project, arch)

print("Testing Backend...")
backend = backend_agent(project, arch, db)

print("Testing QA...")
qa = qa_agent(project, backend)

print("Testing DevOps...")
devops = devops_agent(project, arch)

print("Testing Risk...")
risk = risk_agent(project, arch)

print("Testing Cost...")
cost = cost_agent(project, arch)

print("Testing Docs...")
docs = docs_agent(
    project,
    pm,
    arch,
    db,
    backend,
    qa,
    devops,
    risk,
    cost
)

print("\nSUCCESS!\n")
print(docs[:1000])