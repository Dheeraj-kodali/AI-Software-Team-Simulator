from llm import llm

def qa_agent(project,backend_output):

    prompt = f"""
    You are a QA Engineer.

    Project: {project}

    Backend Design:

    {backend_output}

    Generate:

    1. Functional Test Cases
    2. Negative Test Cases
    3. API Testing Plan
    4. Security Testing
    5. Performance Testing
    """

    response = llm.invoke(prompt)

    return response.content