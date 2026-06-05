from sdk.ai_sdk import AISDK


def qa_agent(project, backend_output):

    prompt = f"""
    You are a Senior QA Engineer.

    Project:
    {project}

    Backend Output:

    {backend_output}

    Generate:

    1. Functional Test Cases
    2. Negative Test Cases
    3. API Testing Plan
    4. Security Testing Strategy
    5. Performance Testing Strategy
    6. Load Testing Plan
    7. Regression Testing Plan
    8. Test Automation Strategy
    9. Bug Tracking Process

    Maximum 1200 words.

    Use:
    - Clear Headings
    - Bullet Points
    - Professional Formatting
    """

    return AISDK.generate(
        prompt,
        "QA Agent"
    )