from llm import llm

def database_agent(project,architecture_output):

    prompt = f"""
    You are a Database Architect.

    Project: {project}

    Based on the architecture below:

    {architecture_output}

    Generate:

    1. Database Design
    2. Tables
    3. Relationships
    4. Primary Keys
    5. Foreign Keys
    6. Sample SQL Schema
    """

    response = llm.invoke(prompt)

    return response.content