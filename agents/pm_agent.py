from sdk.ai_sdk import AISDK

def pm_agent(project):

    prompt = f"""
    You are a Senior Product Manager.

    Project:
    {project}

    Generate:

    1. Business Requirements
    2. Functional Requirements
    3. User Stories
    4. Success Criteria

    Maximum 1200 words.
    """

    return AISDK.generate(
        prompt,
        "PM Agent"
    )