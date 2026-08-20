"""
Part 5 - Policy Knowledge Base

A small, self-authored Flipkart-style policy knowledge base.

Each document is intentionally short and focused on one
support-policy topic.

The document_id is kept stable so that later RAG chunks
can be mapped back to their parent document for retrieval
evaluation.
"""


POLICY_DOCUMENTS = [
    {
        "document_id": "policy_return_apparel",
        "title": "Return Window for Apparel",
        "text": (
            "Apparel products can generally be returned within "
            "7 days of delivery if they are unused, unwashed, "
            "and have their original tags and packaging intact."
        ),
    },
    {
        "document_id": "policy_return_electronics",
        "title": "Return Window for Electronics",
        "text": (
            "Electronics products can generally be returned within "
            "7 days of delivery when the product is unused or has "
            "a valid defect, and all original accessories and packaging "
            "are available."
        ),
    },
    {
        "document_id": "policy_return_footwear",
        "title": "Return Window for Footwear",
        "text": (
            "Footwear can generally be returned within 7 days of delivery. "
            "The footwear should be unused, undamaged, and returned with "
            "the original box, tags, and accessories."
        ),
    },
    {
        "document_id": "policy_return_beauty",
        "title": "Return Window for Beauty Products",
        "text": (
            "Beauty and personal-care products are generally eligible "
            "for return within 7 days only when the item is unopened, "
            "unused, and in its original packaging."
        ),
    },
    {
        "document_id": "policy_cod_refund",
        "title": "COD Refund Timeline",
        "text": (
            "For eligible cash-on-delivery returns, the refund is normally "
            "processed after the returned product passes the required "
            "quality check. The refund is generally issued to the customer's "
            "eligible bank account or supported refund method."
        ),
    },
    {
        "document_id": "policy_prepaid_refund",
        "title": "Prepaid Order Refund Timeline",
        "text": (
            "For eligible prepaid returns, the refund is initiated after "
            "the returned product is received and the required verification "
            "is completed. The amount is generally credited back to the "
            "original payment method."
        ),
    },
    {
        "document_id": "policy_delivery_sla",
        "title": "Delivery Service Level",
        "text": (
            "The estimated delivery date shown for an order is based on "
            "the delivery address, seller processing time, courier network, "
            "and product availability. Delivery estimates can change because "
            "of operational or external delays."
        ),
    },
    {
        "document_id": "policy_reverse_pickup",
        "title": "Reverse Pickup Eligibility",
        "text": (
            "Reverse pickup is available for eligible return requests "
            "depending on the product category, delivery location, seller "
            "policy, and courier availability. Customers should keep the "
            "product packed and ready for pickup when a pickup is scheduled."
        ),
    },
    {
        "document_id": "policy_damaged_product",
        "title": "Damaged Product Returns",
        "text": (
            "If a product arrives damaged, the customer should report the "
            "issue as soon as possible through the order support process. "
            "The request may require photographs or other information to "
            "verify the reported damage."
        ),
    },
    {
        "document_id": "policy_wrong_product",
        "title": "Wrong Product Received",
        "text": (
            "If the delivered product is different from the product ordered, "
            "the customer can raise a support request for an eligible return "
            "or replacement. The request may be reviewed against the order "
            "details and delivered item."
        ),
    },
    {
        "document_id": "policy_exchange",
        "title": "Product Exchange Eligibility",
        "text": (
            "Exchange is available only for products and sellers that support "
            "the exchange option. Eligibility can depend on product category, "
            "size or variant availability, return condition, and the seller's "
            "applicable policy."
        ),
    },
    {
        "document_id": "policy_cancellation",
        "title": "Order Cancellation",
        "text": (
            "An order may be cancelled before it reaches a stage where "
            "cancellation is no longer supported. Once the order has been "
            "shipped or handed to the delivery network, cancellation options "
            "may be limited."
        ),
    },
    {
        "document_id": "policy_non_returnable",
        "title": "Non-Returnable Products",
        "text": (
            "Certain products may not be eligible for return because of "
            "hygiene, safety, consumable, personalized, or other category-"
            "specific restrictions. The applicable return eligibility is "
            "shown with the product or order information."
        ),
    },
    {
        "document_id": "policy_missing_accessories",
        "title": "Missing Accessories",
        "text": (
            "If an ordered product arrives without an expected accessory, "
            "the customer should report the missing item through order support. "
            "The request can be checked against the product listing and order "
            "details before an appropriate resolution is provided."
        ),
    },
]


def get_policy_documents():
    """
    Return the complete policy knowledge base.
    """
    return POLICY_DOCUMENTS


if __name__ == "__main__":
    print("=== POLICY KNOWLEDGE BASE ===")
    print(f"Total documents: {len(POLICY_DOCUMENTS)}")
    print()

    for document in POLICY_DOCUMENTS:
        print(
            f"{document['document_id']}: "
            f"{document['title']}"
        )