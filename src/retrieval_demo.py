"""
Simple semantic-retrieval demonstration for the
Multimodal Image-to-Story Generation project.

This example uses sentence embeddings and FAISS to retrieve
the most relevant story contexts for a text-based image description.
"""

from typing import List, Tuple

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"


def build_index(
    texts: List[str],
    model: SentenceTransformer,
) -> Tuple[faiss.IndexFlatIP, np.ndarray]:
    """Create a cosine-similarity FAISS index from text examples."""
    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True,
    ).astype("float32")

    index = faiss.IndexFlatIP(embeddings.shape[1])
    index.add(embeddings)

    return index, embeddings


def retrieve(
    query: str,
    texts: List[str],
    model: SentenceTransformer,
    index: faiss.IndexFlatIP,
    top_k: int = 3,
) -> List[Tuple[str, float]]:
    """Retrieve the most semantically relevant text examples."""
    query_embedding = model.encode(
        [query],
        convert_to_numpy=True,
        normalize_embeddings=True,
    ).astype("float32")

    scores, indices = index.search(query_embedding, top_k)

    results: List[Tuple[str, float]] = []

    for item_index, score in zip(indices[0], scores[0]):
        results.append((texts[item_index], float(score)))

    return results


def main() -> None:
    examples = [
        "A family is having dinner together at home.",
        "Children are playing football in a public park.",
        "A student is reading a book inside a library.",
        "People are shopping in a busy city market.",
        "A doctor is speaking with a patient in a clinic.",
    ]

    query = "Several children are enjoying an outdoor sports activity."

    model = SentenceTransformer(MODEL_NAME)
    index, _ = build_index(examples, model)

    results = retrieve(
        query=query,
        texts=examples,
        model=model,
        index=index,
        top_k=3,
    )

    print(f"Query: {query}\n")

    for rank, (text, score) in enumerate(results, start=1):
        print(f"{rank}. {text}")
        print(f"   Similarity: {score:.4f}")


if __name__ == "__main__":
    main()
