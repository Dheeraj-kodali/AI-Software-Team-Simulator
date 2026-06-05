from sdk.ai_sdk import AISDK


def database_agent(project, architecture_output):

    prompt = f"""
    You are a Senior Database Architect.

    Project:
    {project}

    Architecture Output:

    {architecture_output}

    Generate:

    1. Database Design
    2. Entity Relationship Design
    3. Tables
    4. Relationships
    5. Primary Keys
    6. Foreign Keys
    7. Indexing Strategy
    8. Database Security Considerations
    9. Sample SQL Schema

    Maximum 1200 words.

    Use:
    - Clear Headings
    - Bullet Points
    - Professional Formatting
    """

    return AISDK.generate(
        prompt,
        "Database Agent"
    )