from part4_langgraph_agent.graph import support_graph


def run_support_agent(order_id):
    """
    Run the LangGraph support agent for an order.
    """

    initial_state = {
        "order_id": order_id
    }

    result = support_graph.invoke(initial_state)

    return result


if __name__ == "__main__":

    print("=== LANGGRAPH SUPPORT AGENT ===")

    test_order_id = 1

    result = run_support_agent(test_order_id)

    print("\n=== SUPPORT RESPONSE ===\n")

    print(result["response"])