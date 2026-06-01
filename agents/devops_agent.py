from llm import llm

def devops_agent(project, architecture_output):

    prompt = f"""
    You are a DevOps Engineer.

    Project: {project}

    Architecture:

    {architecture_output}

    Generate:

    1. Deployment Strategy
    2. Docker Setup
    3. CI/CD Pipeline
    4. Monitoring Strategy
    5. Cloud Recommendations
    """

    response = llm.invoke(prompt)

    return response.content