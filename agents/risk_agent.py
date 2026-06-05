from sdk.ai_sdk import AISDK


def risk_agent(project, architect_output):

    prompt = f"""
    You are a Senior Software Risk Analyst.

    Project:
    {project}

    Architecture Output:

    {architect_output}

    Analyze and Generate:

    1. Security Risks
    2. Scalability Risks
    3. Performance Risks
    4. Cost Risks
    5. Deployment Risks
    6. Compliance Risks
    7. Data Privacy Risks
    8. Disaster Recovery Risks

    For each risk provide:

    - Description
    - Impact
    - Probability
    - Mitigation Strategy

    Maximum 1200 words.

    Use:
    - Clear Headings
    - Bullet Points
    - Professional Formatting
    """

    return AISDK.generate(
        prompt,
        "Risk Agent"
    )