from sdk.ai_sdk import AISDK


def cost_agent(project, architect_output):

    prompt = f"""
    You are a Senior Project Estimation Manager.

    Project:
    {project}

    Architecture Output:

    {architect_output}

    Generate:

    1. Recommended Team Structure
    2. Team Size Estimation
    3. Development Timeline
    4. Infrastructure Cost Estimation
    5. Monthly Cloud Cost
    6. Maintenance Cost
    7. Third-Party Service Costs
    8. Project Complexity Assessment
    9. Budget Optimization Recommendations

    For each estimate provide:

    - Assumptions
    - Estimated Cost
    - Justification

    Maximum 1200 words.

    Use:
    - Clear Headings
    - Bullet Points
    - Professional Formatting
    """

    return AISDK.generate(
        prompt,
        "Cost Agent"
    )