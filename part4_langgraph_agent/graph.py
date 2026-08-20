from langgraph.graph import StateGraph, START, END

from part4_langgraph_agent.state import SupportAgentState

from part4_langgraph_agent.nodes import (
    intent_node,
    policy_node,
    lookup_order_node,
    return_risk_node,
    product_category_node,
    response_node,
    route_by_intent,
)


def build_support_graph():
    """
    Build the LangGraph support agent workflow.

    Supported flows:

        Return Risk
            START
              ↓
           Intent
              ↓
        Lookup Order
              ↓
         Return Risk
              ↓
          Response
              ↓
             END


        Product Category
            START
              ↓
           Intent
              ↓
       Product Category
              ↓
          Response
              ↓
             END


        Policy Question
            START
              ↓
           Intent
              ↓
           Policy RAG
              ↓
             END
    """

    graph = StateGraph(SupportAgentState)

    # ---------------------------------------------------------
    # Add nodes
    # ---------------------------------------------------------

    graph.add_node(
        "intent",
        intent_node
    )

    graph.add_node(
        "policy",
        policy_node
    )

    graph.add_node(
        "lookup_order",
        lookup_order_node
    )

    graph.add_node(
        "return_risk",
        return_risk_node
    )

    graph.add_node(
        "product_category",
        product_category_node
    )

    graph.add_node(
        "response",
        response_node
    )

    # ---------------------------------------------------------
    # START → Intent
    # ---------------------------------------------------------

    graph.add_edge(
        START,
        "intent"
    )

    # ---------------------------------------------------------
    # Intent → appropriate flow
    # ---------------------------------------------------------

    graph.add_conditional_edges(
        "intent",
        route_by_intent,
        {
            "return_risk": "lookup_order",
            "product_category": "product_category",
            "policy_question": "policy",
        },
    )

    # ---------------------------------------------------------
    # Policy RAG flow
    #
    # policy_node performs:
    # retrieval → generation
    # ---------------------------------------------------------

    graph.add_edge(
        "policy",
        END
    )

    # ---------------------------------------------------------
    # Return-risk flow
    # ---------------------------------------------------------

    graph.add_edge(
        "lookup_order",
        "return_risk"
    )

    graph.add_edge(
        "return_risk",
        "response"
    )

    # ---------------------------------------------------------
    # Product-category flow
    # ---------------------------------------------------------

    graph.add_edge(
        "product_category",
        "response"
    )

    # ---------------------------------------------------------
    # Response → END
    # ---------------------------------------------------------

    graph.add_edge(
        "response",
        END
    )

    return graph.compile()


# -------------------------------------------------------------
# Create compiled graph
# -------------------------------------------------------------

support_graph = build_support_graph()