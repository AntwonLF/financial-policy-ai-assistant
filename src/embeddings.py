# Financial Policy AI Assistant
# Phase 2: Embeddings for policy chunks

from functools import lru_cache
from sentence_transformers import SentenceTransformer

@lru_cache(maxsize=1)
def get_embedding_model():
    # Load and reuse one embedding model instance
    return SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2"
    )

def generate_embeddings(chunks: list[str]):
    # Get the cached embedding model instance
    model = get_embedding_model()

    # Convert text chunks into normalized vectors
    embeddings = model.encode(
        chunks,
        normalize_embeddings=True
    )

    return embeddings