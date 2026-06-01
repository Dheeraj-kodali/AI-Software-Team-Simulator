from llm import llm

def architect_agent(project,pm_output):

    prompt = f"""
    You are a Senior Software Architect.

    Based on the Product Manager requirements below:

    {pm_output}

    Generate:

    1. System Architecture
    2. Recommended Tech Stack
    3. High-Level Components
    4. Scalability Considerations
    5. Security Considerations
    """

    response = llm.invoke(prompt)

    return response.content