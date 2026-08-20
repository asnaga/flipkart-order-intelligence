"""
Part 5 - RAG
Embedding / vectorization layer.

The project initially uses TF-IDF vectors instead of neural
sentence embeddings.

Reason:
- Lightweight
- No PyTorch dependency
- No ONNX Runtime dependency
- Works reliably in the current Windows environment
- Sufficient for the small policy knowledge base

The vectorization interface is kept isolated so that a
sentence-transformer backend can be introduced later
without changing the retrieval or LangGraph layers.
"""

from typing import List, Dict, Any

from sklearn.feature_extraction.text import TfidfVectorizer


class PolicyVectorizer:
    """
    Convert policy chunks into TF-IDF vectors.

    This class acts as the vectorization abstraction for the
    RAG pipeline.
    """

    def __init__(self):
        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            stop_words="english",
            ngram_range=(1, 2)
        )

        self.vectors = None
        self.chunks: List[Dict[str, Any]] = []

    def fit(self, chunks: List[Dict[str, Any]]):
        """
        Fit the TF-IDF vectorizer on policy chunks.

        Args:
            chunks: List of policy chunk dictionaries.

        Returns:
            TF-IDF matrix containing vectors for all chunks.
        """

        if not chunks:
            raise ValueError("No policy chunks provided.")

        self.chunks = chunks

        texts = [
            chunk["text"]
            for chunk in chunks
        ]

        self.vectors = self.vectorizer.fit_transform(texts)

        return self.vectors

    def transform_query(self, query: str):
        """
        Convert a user query into the same TF-IDF vector space
        used by the policy chunks.

        Args:
            query: User's policy question.

        Returns:
            TF-IDF vector for the query.
        """

        if self.vectors is None:
            raise RuntimeError(
                "Vectorizer has not been fitted. "
                "Call fit() before transform_query()."
            )

        if not query or not query.strip():
            raise ValueError("Query cannot be empty.")

        return self.vectorizer.transform([query])

    def get_chunks(self):
        """
        Return the policy chunks used during fitting.
        """

        return self.chunks


def build_vectorizer(chunks: List[Dict[str, Any]]) -> PolicyVectorizer:
    """
    Convenience function to create and fit a policy vectorizer.
    """

    vectorizer = PolicyVectorizer()
    vectorizer.fit(chunks)

    return vectorizer


if __name__ == "__main__":
    from part5_rag.chunking import get_policy_chunks

    print("=== POLICY VECTOR EMBEDDINGS ===")

    chunks = get_policy_chunks()

    vectorizer = build_vectorizer(chunks)

    print(f"Total chunks: {len(chunks)}")
    print(f"Vector dimensions: {vectorizer.vectors.shape[1]}")
    print(f"Vector matrix shape: {vectorizer.vectors.shape}")

    query = "How many days can I return footwear?"

    query_vector = vectorizer.transform_query(query)

    print("\nTest query:")
    print(query)

    print("\nQuery vector shape:")
    print(query_vector.shape)

    print("\nVectorization successful.")