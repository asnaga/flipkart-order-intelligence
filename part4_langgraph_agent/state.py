from typing import TypedDict, Optional, List, Dict, Any


class SupportAgentState(TypedDict, total=False):
    """
    State shared between LangGraph nodes.

    The state contains information required by both the
    traditional support-agent flows and the Part 5 RAG flow.
    """

    # ---------------------------------------------------------
    # User input
    # ---------------------------------------------------------

    order_id: int
    user_query: str

    # ---------------------------------------------------------
    # Intent
    # ---------------------------------------------------------

    intent: Optional[str]

    # ---------------------------------------------------------
    # Order intelligence
    # ---------------------------------------------------------

    order: Optional[dict]
    return_risk: Optional[dict]
    product_category: Optional[dict]

    # ---------------------------------------------------------
    # RAG
    # ---------------------------------------------------------

    retrieved_policy_chunks: Optional[List[Dict[str, Any]]]

    # ---------------------------------------------------------
    # Final response
    # ---------------------------------------------------------

    response: Optional[str]

    # ---------------------------------------------------------
    # Status
    # ---------------------------------------------------------

    status: Optional[str]