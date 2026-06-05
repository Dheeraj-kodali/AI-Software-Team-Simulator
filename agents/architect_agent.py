from sdk.ai_sdk import AISDK


def architect_agent(project, pm_output):

    prompt = f"""
    You are a Senior Software Architect.

    Project:
    {project}

    Product Manager Output:

    {pm_output}

    Generate:

    1. System Architecture
    2. Recommended Tech Stack
    3. High-Level Components
    4. Scalability Considerations
    5. Security Considerations
    6. Deployment Architecture
    7. API Design Strategy

    Maximum 1200 words.

    Use:
    - Clear Headings
    - Bullet Points
    - Professional Formatting
    """

    return AISDK.generate(
        prompt,
        "Architect Agent"
    )