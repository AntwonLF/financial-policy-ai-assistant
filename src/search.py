
# Financial Policy AI Assistant
# Phase 3: Semantic Search

from .embeddings import generate_embeddings


def search_policies(question: str, records: list[dict], embeddings, top_k: int = 3):

    # Handle empty questions or missing records
    if not question.strip() or not records:
        return []

    # Ensure each record has a corresponding embedding
    if len(records) != len(embeddings):
        raise ValueError("Records and embeddings must have matching lengths.")

    # Convert the user's question into an embedding
    question_vector = generate_embeddings([question])[0]

    # Calculate similarity against every policy chunk
    scores = embeddings @ question_vector

    # Rank results from highest similarity to lowest
    ranked_indexes = scores.argsort()[::-1][:top_k]

    # Collect the most relevant records
    results = []

    for index in ranked_indexes:
        record = records[int(index)].copy()
        record["similarity"] = float(scores[index])
        results.append(record)

    return results
