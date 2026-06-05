from sdk.ai_sdk import AISDK


def docs_agent(
    project,
    pm_output,
    architect_output,
    database_output,
    backend_output,
    qa_output,
    devops_output,
    risk_output,
    cost_output
):

    prompt = f"""
    Project: {project}

    Product Management Summary:
    {pm_output}

    Architecture Summary:
    {architect_output}

    Database Summary:
    {database_output}

    Backend Summary:
    {backend_output}

    QA Summary:
    {qa_output}

    DevOps Summary:
    {devops_output}

    Risk Summary:
    {risk_output}

    Cost Summary:
    {cost_output}

    Create a professional Software Design Document.

    Include:

    1. Executive Summary
    2. Project Overview
    3. Architecture Overview
    4. Database Design Summary
    5. Backend Design Summary
    6. Testing Strategy
    7. Deployment Strategy
    8. Risk Assessment
    9. Cost Estimation
    10. Conclusion

    Maximum 800 words.
    Use proper headings.
    """

    return AISDK.generate(
        prompt,
        "Documentation Agent"
    )
