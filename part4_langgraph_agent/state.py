from typing import TypedDict, Optional


class SupportAgentState(TypedDict, total=False):
    """
    State shared between LangGraph nodes.
    """

    order_id: int

    order: Optional[dict]

    return_risk: Optional[dict]

    product_category: Optional[dict]

    response: Optional[str]

    status: Optional[str]