from sdk.ai_sdk import AISDK


def devops_agent(project, architecture_output):

    prompt = f"""
    You are a Senior DevOps Engineer.

    Project:
    {project}

    Architecture Output:

    {architecture_output}

    Generate:

    1. Deployment Strategy
    2. Docker Setup
    3. CI/CD Pipeline
    4. Monitoring Strategy
    5. Logging Strategy
    6. Cloud Recommendations
    7. Kubernetes Deployment Plan
    8. Backup & Recovery Strategy
    9. Infrastructure Security Best Practices

    Maximum 1200 words.

    Use:
    - Clear Headings
    - Bullet Points
    - Professional Formatting
    """

    return AISDK.generate(
        prompt,
        "DevOps Agent"
    )