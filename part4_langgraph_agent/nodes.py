from part3_support_agent.order_lookup import get_order
from part3_support_agent.return_risk_tool import get_return_risk
from part3_support_agent.product_category_tool import get_product_category

from part4_langgraph_agent.state import SupportAgentState


def lookup_order_node(state: SupportAgentState):
    """
    Look up the order using the existing Part 3 order lookup tool.
    """

    order_id = state["order_id"]

    order = get_order(order_id)

    if order is None:
        return {
            "status": "Order not found"
        }

    return {
        "order": order,
        "status": "Order found"
    }


def return_risk_node(state: SupportAgentState):
    """
    Calculate return risk using the existing Part 3 return-risk tool.
    """

    order_id = state["order_id"]

    return_risk = get_return_risk(order_id)

    return {
        "return_risk": return_risk
    }


def product_category_node(state: SupportAgentState):
    """
    Predict product category using the existing Part 3 product-category tool.
    """

    order_id = state["order_id"]

    product_category = get_product_category(order_id)

    return {
        "product_category": product_category
    }


def response_node(state: SupportAgentState):
    """
    Generate a human-readable support response.
    """

    if state.get("status") == "Order not found":
        return {
            "response": (
                f"Sorry, order {state['order_id']} was not found."
            )
        }

    order = state["order"]
    risk = state["return_risk"]
    category = state["product_category"]

    risk_label = "High" if risk["return_risk"] == 1 else "Low"

    response = f"""
Order ID: {order['order_id']}

Product Category: {category['product_category']}
Price: ₹{order['price_inr']:.2f}
Payment Method: {order['payment_method']}
Delivery Days: {order['delivery_days']}
Customer Tenure: {order['customer_tenure_days']} days
Previous Orders: {order['num_previous_orders']}
Previous Returns: {order['num_previous_returns']}

Return Risk: {risk_label}
Return Probability: {risk['return_probability']:.2%}

The order is currently predicted to have a {risk_label.lower()} return risk.
"""

    return {
        "response": response.strip()
    }