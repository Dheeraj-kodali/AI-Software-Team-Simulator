from sdk.ai_sdk import AISDK

text = """
Hospital Management System

Modules:
Patient Management
Doctor Management
Billing
Appointments
Laboratory
Pharmacy
"""

summary = AISDK.summarize(text)

print(summary)