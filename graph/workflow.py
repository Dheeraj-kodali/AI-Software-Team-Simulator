from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents.pm_agent import pm_agent
from agents.architect_agent import architect_agent
from agents.database_agent import database_agent
from agents.backend_agent import backend_agent
from agents.qa_agent import qa_agent
from agents.devops_agent import devops_agent
from agents.docs_agent import docs_agent
from agents.risk_agent import risk_agent
from agents.cost_agent import cost_agent
from utils.save_output import save_output
from sdk.ai_sdk import AISDK


# Shared State
class ProjectState(TypedDict):
    project: str

    pm_output: str
    pm_summary: str

    architect_output: str
    architect_summary: str

    database_output: str
    database_summary: str

    backend_output: str
    backend_summary: str

    qa_output: str
    qa_summary: str

    devops_output: str
    devops_summary: str

    risk_output: str
    risk_summary: str

    cost_output: str
    cost_summary: str

    docs_output: str


# --------------------------
# PM Node
# --------------------------
def pm_node(state):

    print("Running PM Agent...")

    result = pm_agent(state["project"])

    summary = AISDK.summarize(result)

    print("PM Agent Completed")

    return {
        "pm_output": result,
        "pm_summary": summary
    }


# --------------------------
# Architect Node
# --------------------------
def architect_node(state):

    print("Running Architect Agent...")

    result = architect_agent(
        state["project"],
        state["pm_summary"]
    )

    summary = AISDK.summarize(result)

    print("Architect Agent Completed")

    return {
        "architect_output": result,
        "architect_summary": summary
    }


# --------------------------
# Database Node
# --------------------------
def database_node(state):

    print("Running Database Agent...")

    result = database_agent(
        state["project"],
        state["architect_summary"]
    )

    summary = AISDK.summarize(result)

    print("Database Agent Completed")

    return {
        "database_output": result,
        "database_summary": summary
    }


# --------------------------
# Backend Node
# --------------------------
def backend_node(state):

    print("Running Backend Agent...")

    result = backend_agent(
        state["project"],
        state["architect_summary"],
        state["database_summary"]
    )

    summary = AISDK.summarize(result)

    print("Backend Agent Completed")

    return {
        "backend_output": result,
        "backend_summary": summary
    }


# --------------------------
# QA Node
# --------------------------
def qa_node(state):

    print("Running QA Agent...")

    result = qa_agent(
        state["project"],
        state["backend_summary"]
    )

    summary = AISDK.summarize(result)

    print("QA Agent Completed")

    return {
        "qa_output": result,
        "qa_summary": summary
    }


# --------------------------
# DevOps Node
# --------------------------
def devops_node(state):

    print("Running DevOps Agent...")

    result = devops_agent(
        state["project"],
        state["architect_summary"]
    )

    summary = AISDK.summarize(result)

    print("DevOps Agent Completed")

    return {
        "devops_output": result,
        "devops_summary": summary
    }

# --------------------------
# Risk Node
def risk_node(state):

    print("Running Risk Agent...")

    result = risk_agent(
        state["project"],
        state["architect_summary"]
    )

    summary = AISDK.summarize(result)

    print("Risk Agent Completed")

    return {
        "risk_output": result,
        "risk_summary": summary
    }


# --------------------------
# Cost Node
def cost_node(state):

    print("Running Cost Agent...")

    result = cost_agent(
        state["project"],
        state["architect_summary"]
    )

    summary = AISDK.summarize(result)

    print("Cost Agent Completed")

    return {
        "cost_output": result,
        "cost_summary": summary
    }


# --------------------------
# Docs Node
# --------------------------
def docs_node(state):

    print("Running Docs Agent...")

    result = docs_agent(
    state["project"],
    state["pm_summary"],
    state["architect_summary"],
    state["database_summary"],
    state["backend_summary"],
    state["qa_summary"],
    state["devops_summary"],
    state["cost_summary"],
    state["risk_summary"]
    )

    print("Docs Agent Completed")
    print("ABOUT TO SAVE FILE")

    save_output(
         state["project"],
        result
    )

    return {
        "docs_output": result
    }





# --------------------------
# Build Graph
# --------------------------
builder = StateGraph(ProjectState)

builder.add_node("pm", pm_node)
builder.add_node("architect", architect_node)
builder.add_node("database", database_node)
builder.add_node("backend", backend_node)
builder.add_node("qa", qa_node)
builder.add_node("devops", devops_node)
builder.add_node("risk", risk_node)
builder.add_node("cost", cost_node)
builder.add_node("docs", docs_node)


# Flow
builder.set_entry_point("pm")

builder.add_edge("pm", "architect")
builder.add_edge("architect", "database")
builder.add_edge("database", "backend")
builder.add_edge("backend", "qa")
builder.add_edge("qa", "devops")
builder.add_edge("devops", "risk")
builder.add_edge("risk", "cost")
builder.add_edge("cost", "docs")
builder.add_edge("docs", END)


# Compile
software_team_graph = builder.compile()
def run_workflow(project_name):
    result = software_team_graph.invoke(
        {
            "project": project_name
        }
    )
    return result