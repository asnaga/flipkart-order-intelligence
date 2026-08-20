"""
Part 5 - RAG
Policy answer generation layer.

This module generates a grounded answer from the policy
chunks returned by the retrieval layer.

The current implementation is deterministic and does not
require an external LLM.

The design keeps the generation layer isolated so that an
LLM-based generator can be introduced later without changing
the retrieval or LangGraph layers.
"""

from typing import List, Dict, Any


def generate_policy_answer(
    query: str,
    retrieved_chunks: List[Dict[str, Any]]
) -> str:
    """
    Generate a policy answer using retrieved policy chunks.

    Args:
        query:
            Original user policy question.

        retrieved_chunks:
            Policy chunks returned by retrieve_policy().

    Returns:
        A grounded policy answer.
    """

    if not query or not query.strip():
        return "Please provide a policy-related question."

    if not retrieved_chunks:
        return (
            "I could not find a relevant policy in the "
            "knowledge base."
        )

    # Use the highest-ranked retrieved document.
    best_chunk = retrieved_chunks[0]

    title = best_chunk.get("title", "Policy")
    text = best_chunk.get("text", "").strip()

    if not text:
        return (
            "I found a relevant policy document, but it "
            "does not contain enough information to answer "
            "the question."
        )

    return f"{text}"


if __name__ == "__main__":
    from part5_rag.retrieval import retrieve_policy

    print("=== POLICY ANSWER GENERATOR ===")

    test_queries = [
        "How many days can I return footwear?",
        "When will I get my prepaid refund?",
        "Can I cancel my order after it has shipped?",
    ]

    for query in test_queries:
        print("\n" + "=" * 70)
        print(f"Question: {query}")
        print("=" * 70)

        results = retrieve_policy(query, top_k=1)

        answer = generate_policy_answer(
            query,
            results
        )

        print("\nAnswer:")
        print(answer)