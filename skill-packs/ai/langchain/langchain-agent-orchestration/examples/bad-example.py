# BAD — unbounded loop, arbitrary code exec, no tool schema
while True:
    response = llm(f"Do anything to answer: {user_input}")
    exec(response)  # never
