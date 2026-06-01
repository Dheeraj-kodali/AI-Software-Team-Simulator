from llm import llm

def cost_agent(project, architect_output):

    prompt = f"""
    You are a Senior Project Estimation Manager.

    Project:
    {project}

    Architecture:
    {architect_output}

    Estimate:

    1. Team Size
    2. Development Time
    3. Monthly Cloud Cost
    4. Maintenance Cost
    5. Project Complexity

    Give concise output.
    """

    response = llm.invoke(prompt)

    return response.content