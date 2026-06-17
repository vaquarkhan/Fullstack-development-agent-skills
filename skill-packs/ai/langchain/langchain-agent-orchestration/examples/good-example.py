# GOOD — bounded tool loop, structured output, timeout on LLM call
@tool
def lookup_order(order_id: str) -> str:
    """Fetch order status by id."""
    return order_service.get_status(order_id)

agent = create_react_agent(llm, tools=[lookup_order], checkpointer=memory)
result = agent.invoke(
    {"messages": [("user", query)]},
    config={"recursion_limit": 8, "timeout": 30},
)
