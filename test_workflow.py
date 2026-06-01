from graph.workflow import run_workflow

result = run_workflow(
    "Hospital Management System"
)

print("\nPM OUTPUT\n")
print(result["pm_output"])

print("\nARCHITECT OUTPUT\n")
print(result["architect_output"])

print("\nDATABASE OUTPUT\n")
print(result["database_output"])

print("\nBACKEND OUTPUT\n")
print(result["backend_output"])

print("\nQA OUTPUT\n")
print(result["qa_output"])

print("\nDEVOPS OUTPUT\n")
print(result["devops_output"])

print("\nDOCS OUTPUT\n")
print(result["docs_output"])