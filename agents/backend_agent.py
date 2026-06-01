from llm import llm

def backend_agent(project,architecture_output, database_output):

    prompt = f"""
    You are a Senior Backend Engineer.

    Project: {project}
    
    Architecture:
    
    {architecture_output}

    Database Design:

    {database_output}

    Generate:

    1. API Endpoints
    2. Request/Response Examples
    3. Authentication Flow
    4. Backend Folder Structure
    5. Business Logic Overview
    """

    response = llm.invoke(prompt)

    return response.content