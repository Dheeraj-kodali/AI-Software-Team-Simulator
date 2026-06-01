from llm import llm

def pm_agent(project):

    prompt = f"""
    You are a Product Manager.

    Project:
    {project}

    Generate:

    1. Business requirements
    2. Functional requirements
    3. User stories
    """

    response = llm.invoke(prompt)

    return response.content