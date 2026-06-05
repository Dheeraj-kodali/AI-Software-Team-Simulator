from sdk.ai_sdk import AISDK


def backend_agent(project, architecture_output, database_output):

    prompt = f"""
    You are a Senior Backend Engineer.

    Project:
    {project}

    Architecture Output:

    {architecture_output}

    Database Output:

    {database_output}

    Generate:

    1. REST API Endpoints
    2. Request/Response Examples
    3. Authentication & Authorization Flow
    4. Backend Folder Structure
    5. Business Logic Overview
    6. Error Handling Strategy
    7. Logging Strategy
    8. Security Best Practices
    9. Deployment Considerations

    Maximum 1200 words.

    Use:
    - Clear Headings
    - Bullet Points
    - Professional Formatting
    """

    return AISDK.generate(
        prompt,
        "Backend Agent"
    )