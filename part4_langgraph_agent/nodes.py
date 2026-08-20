from part3_support_agent.order_lookup import get_order
from part3_support_agent.return_risk_tool import get_return_risk
from part3_support_agent.product_category_tool import get_product_category

from part4_langgraph_agent.state import SupportAgentState

from part5_rag.retrieval import retrieve_policy
from part5_rag.generator import generate_policy_answer


def intent_node(state: SupportAgentState):
    """
    Determine what the user is asking the support agent to do.

    Supported intents:
    - policy_question
    - return_risk
    - product_category
    """

    user_query = state.get("user_query", "").lower().strip()

    # --------------------------------------------------
    # Return-risk related questions
    # --------------------------------------------------

    return_risk_keywords = [
        "return risk",
        "return probability",
        "risk of return",
        "likely to return",
        "will this order be returned",
        "return prediction",
        "chance of return",
        "probability of return",
        "will my order be returned",
        "chance that my order will be returned",
        "chance my order will be returned",
        "likelihood of return",
        "likelihood that my order will be returned",
        "how likely is my order to be returned",
    ]

    if any(keyword in user_query for keyword in return_risk_keywords):
        return {
            "intent": "return_risk"
        }

    # --------------------------------------------------
    # Product-category related questions
    # --------------------------------------------------

    category_keywords = [
        "product category",
        "which category",
        "what category",
        "classify product",
        "classify this product",
        "product classification",
        "what type of product",
        "type of product",
    ]

    if any(keyword in user_query for keyword in category_keywords):
        return {
            "intent": "product_category"
        }

    # --------------------------------------------------
    # Policy questions
    # --------------------------------------------------

    policy_keywords = [
        "return policy",
        "refund policy",
        "exchange policy",
        "cancellation policy",
        "delivery policy",
        "return window",
        "how many days can i return",
        "when will i get my refund",
        "can i return",
        "can i cancel",
        "can i exchange",
        "damaged product",
        "wrong product",
        "missing accessory",
    ]

    if any(keyword in user_query for keyword in policy_keywords):
        return {
            "intent": "policy_question"
        }

    # --------------------------------------------------
    # Default
    # --------------------------------------------------

    return {
        "intent": "policy_question"
    }


def policy_node(state: SupportAgentState):
    """
    Handle policy questions using the Part 5 RAG pipeline.

    Flow:

        User question
             ↓
        Policy retrieval
             ↓
        Retrieved policy chunks
             ↓
        Answer generation
             ↓
        Grounded response
    """

    user_query = state.get("user_query", "")

    # ---------------------------------------------------------
    # Retrieve relevant policy chunks
    # ---------------------------------------------------------

    retrieved_chunks = retrieve_policy(
        user_query,
        top_k=3,
    )

    # ---------------------------------------------------------
    # Generate grounded answer
    # ---------------------------------------------------------

    response = generate_policy_answer(
        user_query,
        retrieved_chunks,
    )

    return {
        "retrieved_policy_chunks": retrieved_chunks,
        "response": response,
    }


def route_by_intent(state: SupportAgentState):
    """
    Route the graph according to the detected intent.
    """

    return state.get(
        "intent",
        "policy_question"
    )


def lookup_order_node(state: SupportAgentState):
    """
    Look up the order using the existing Part 3
    order lookup tool.
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
    Calculate return risk using the existing Part 3
    return-risk tool.
    """

    order_id = state["order_id"]

    return_risk = get_return_risk(order_id)

    return {
        "return_risk": return_risk
    }


def product_category_node(state: SupportAgentState):
    """
    Predict product category using the existing Part 3
    product-category tool.
    """

    order_id = state["order_id"]

    product_category = get_product_category(order_id)

    return {
        "product_category": product_category
    }


def response_node(state: SupportAgentState):
    """
    Generate a human-readable support response for
    return-risk and product-category requests.

    Policy questions are handled completely inside
    policy_node().
    """

    # ---------------------------------------------------------
    # Order not found
    # ---------------------------------------------------------

    if state.get("status") == "Order not found":
        return {
            "response": (
                f"Sorry, Order {state['order_id']} "
                f"was not found."
            )
        }

    order = state.get("order")
    risk = state.get("return_risk")
    category = state.get("product_category")

    # ---------------------------------------------------------
    # Return-risk response
    # ---------------------------------------------------------

    if (
        state.get("intent") == "return_risk"
        and order
        and risk
    ):

        risk_label = (
            "High"
            if risk["return_risk"] == 1
            else "Low"
        )

        response = f"""
Order ID: {order['order_id']}

Product Category: {order['product_category']}
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

    # ---------------------------------------------------------
    # Product-category response
    # ---------------------------------------------------------

    if (
        state.get("intent") == "product_category"
        and category
    ):

        if isinstance(category, dict):
            category_label = category.get(
                "product_category",
                category
            )
        else:
            category_label = category

        response = (
            f"The predicted product category is: "
            f"{category_label}"
        )

        return {
            "response": response
        }

    # ---------------------------------------------------------
    # Generic fallback
    # ---------------------------------------------------------

    return {
        "response": (
            "Sorry, I could not determine how to "
            "handle this request."
        )
    }
