from part4_langgraph_agent.graph import support_graph


def run_support_agent(order_id, user_query):
    """
    Run the LangGraph support agent.
    """

    initial_state = {
        "order_id": order_id,
        "user_query": user_query,
    }

    result = support_graph.invoke(initial_state)

    return result


if __name__ == "__main__":

    print("=== LANGGRAPH SUPPORT AGENT ===")

    # --------------------------------------------------
    # Test 1: Return-risk question
    # --------------------------------------------------

    print("\n=== TEST 1: RETURN RISK ===")

    result = run_support_agent(
        1,
        "What is the return risk for my order?"
    )

    print("\n=== SUPPORT RESPONSE ===\n")
    print(result["response"])

    # --------------------------------------------------
    # Test 2: Product-category question
    # --------------------------------------------------

    print("\n=== TEST 2: PRODUCT CATEGORY ===")

    result = run_support_agent(
        1,
        "What is the product category of this order?"
    )

    print("\n=== SUPPORT RESPONSE ===\n")
    print(result["response"])

    # --------------------------------------------------
    # Test 3: Footwear return policy
    # --------------------------------------------------

    print("\n=== TEST 3: FOOTWEAR RETURN POLICY ===")

    result = run_support_agent(
        1,
        "How many days can I return footwear?"
    )

    print("\n=== SUPPORT RESPONSE ===\n")
    print(result["response"])

    # --------------------------------------------------
    # Test 4: Prepaid refund policy
    # --------------------------------------------------

    print("\n=== TEST 4: PREPAID REFUND POLICY ===")

    result = run_support_agent(
        1,
        "When will I get my prepaid refund?"
    )

    print("\n=== SUPPORT RESPONSE ===\n")
    print(result["response"])

    # --------------------------------------------------
    # Test 5: Cancellation policy
    # --------------------------------------------------

    print("\n=== TEST 5: ORDER CANCELLATION POLICY ===")

    result = run_support_agent(
        1,
        "Can I cancel my order after it has shipped?"
    )

    print("\n=== SUPPORT RESPONSE ===\n")
    print(result["response"])