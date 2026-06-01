from llm import llm

def risk_agent(project, architect_output):

    prompt = f"""
    You are a Senior Software Risk Analyst.

    Project:
    {project}

    Architecture:
    {architect_output}

    Identify:

    1. Security Risks
    2. Scalability Risks
    3. Cost Risks
    4. Deployment Risks

    Give recommendations.
    """

    response = llm.invoke(prompt)

    return response.content