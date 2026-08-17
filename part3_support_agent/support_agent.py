from .order_lookup import get_order
from .return_risk_tool import get_return_risk
from .product_category_tool import get_product_category


def support_agent(order_id):
    """
    Generate a complete support summary for an order.
    """

    # Step 1: Look up the order
    order = get_order(order_id)

    if order is None:
        return {
            "order_id": order_id,
            "status": "Order not found"
        }

    # Step 2: Get return risk
    return_risk = get_return_risk(order_id)

    # Step 3: Get product category
    product_category = get_product_category(order_id)

    # Step 4: Combine all tool results
    return {
        "order": order,
        "return_risk": return_risk,
        "product_category": product_category
    }


def format_support_response(result):
    """
    Convert the structured agent result into a
    human-readable customer support response.
    """

    if result.get("status") == "Order not found":
        return f"Sorry, order {result['order_id']} was not found."

    order = result["order"]
    risk = result["return_risk"]
    category = result["product_category"]

    risk_label = "High" if risk["return_risk"] == 1 else "Low"

    response = f"""
=== SUPPORT RESPONSE ===

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

    return response.strip()


if __name__ == "__main__":
    print("=== SUPPORT AGENT ===")

    test_order_id = 1

    result = support_agent(test_order_id)

    print(format_support_response(result))
