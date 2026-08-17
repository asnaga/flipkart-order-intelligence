from langgraph.graph import StateGraph, START, END

from part4_langgraph_agent.state import SupportAgentState

from part4_langgraph_agent.nodes import (
    lookup_order_node,
    return_risk_node,
    product_category_node,
    response_node,
)


def build_support_graph():
    """
    Build the LangGraph support agent workflow.
    """

    graph = StateGraph(SupportAgentState)

    # Add nodes
    graph.add_node("lookup_order", lookup_order_node)
    graph.add_node("return_risk", return_risk_node)
    graph.add_node("product_category", product_category_node)
    graph.add_node("response", response_node)

    # Define workflow
    graph.add_edge(START, "lookup_order")

    graph.add_edge("lookup_order", "return_risk")
    graph.add_edge("return_risk", "product_category")
    graph.add_edge("product_category", "response")

    graph.add_edge("response", END)

    return graph.compile()


support_graph = build_support_graph()