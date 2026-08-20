"""
Part 5 - RAG
Policy retrieval layer.

This module:
1. Loads the policy chunks.
2. Builds the TF-IDF vectorizer.
3. Converts the user query into the same vector space.
4. Calculates cosine similarity.
5. Returns the most relevant policy chunks.
"""

from typing import List, Dict, Any

from sklearn.metrics.pairwise import cosine_similarity

from part5_rag.chunking import get_policy_chunks
from part5_rag.embeddings import build_vectorizer


# -------------------------------------------------------------------
# Build the policy vector store
# -------------------------------------------------------------------

_policy_chunks = get_policy_chunks()

_policy_vectorizer = build_vectorizer(_policy_chunks)


# -------------------------------------------------------------------
# Policy retrieval
# -------------------------------------------------------------------

def retrieve_policy(
    query: str,
    top_k: int = 3
) -> List[Dict[str, Any]]:
    """
    Retrieve the most relevant policy chunks for a user query.

    Args:
        query: User's policy-related question.
        top_k: Number of policy chunks to return.

    Returns:
        List of policy chunks ranked by similarity score.
    """

    if not query or not query.strip():
        return []

    if top_k <= 0:
        return []

    # Convert the user query into the TF-IDF vector space.
    query_vector = _policy_vectorizer.transform_query(query)

    # Get the policy document vectors.
    document_vectors = _policy_vectorizer.vectors

    # Calculate cosine similarity between the query
    # and every policy chunk.
    similarity_scores = cosine_similarity(
        query_vector,
        document_vectors
    )[0]

    # Sort indices by similarity score, highest first.
    ranked_indices = similarity_scores.argsort()[::-1]

    chunks = _policy_vectorizer.get_chunks()

    results = []

    for index in ranked_indices[:top_k]:

        chunk = chunks[index]

        results.append(
            {
                "chunk_id": chunk["chunk_id"],
                "document_id": chunk["document_id"],
                "title": chunk["title"],
                "text": chunk["text"],
                "score": float(similarity_scores[index]),
            }
        )

    return results


# -------------------------------------------------------------------
# Manual test
# -------------------------------------------------------------------

if __name__ == "__main__":

    test_queries = [
        "How many days can I return footwear?",
        "When will I get my prepaid refund?",
        "Can I cancel my order after it has shipped?",
    ]

    print("=== POLICY RETRIEVAL ===")

    for query in test_queries:

        print()
        print("=" * 70)
        print(f"Query: {query}")
        print("=" * 70)

        results = retrieve_policy(
            query,
            top_k=3
        )

        for rank, result in enumerate(results, start=1):

            print()
            print(f"Rank: {rank}")
            print(f"Title: {result['title']}")
            print(f"Score: {result['score']:.4f}")
            print(f"Text: {result['text']}")