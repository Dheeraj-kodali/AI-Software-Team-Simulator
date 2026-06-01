from llm import llm

def docs_agent(
    project,
    pm_output,
    architect_output,
    database_output,
    backend_output,
    qa_output,
    devops_output,
    risk_output,
    cost_output
):

    prompt = f"""
    Project: {project}

    Create a short software design document.

    Include:
    - Project Overview
    - Architecture
    - Database
    - APIs
    - Testing
    - Deployment
    - Risks
    - Cost Analysis

    Keep it under 300 words.
    """

    response = llm.invoke(prompt)

    return response.content