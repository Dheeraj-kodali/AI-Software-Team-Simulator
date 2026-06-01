from llm import llm

response = llm.invoke("What is Python?")

print(response.content)