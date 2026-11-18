# Financial Policy AI Assistant
# Phase 5: Persistent Vector Database Integration

from pathlib import Path
import chromadb

def get_policy_collection():

    # Choose where the database will be stored 
    database_path = (
        Path(__file__).resolve().parent.parent / "chroma_db"
    )

    # Connect to the persistent vector database
    client = chromadb.PersistentClient(
        path=str(database_path)
    )

    # Create or open our policy collection
    collection = client.get_or_create_collection(
        name="financial_policy_chunks",
        configuration={"hnsw": {"space": "cosine"}}
    )

    return collection

def search_stored_policies(question: str, top_k: int = 3) -> list[dict]:
    from .embeddings import generate_embeddings

    # Open our existing database collection
    collection = get_policy_collection()

    # Handle empty existing database collection
    if not question.strip() or collection.count() == 0 or top_k <= 0:
        return []

    # Convert only the question into an embedding
    question_vector = generate_embeddings([question])[0]

    # Search the stored policy embeddings
    results = collection.query(
        query_embeddings=[question_vector.tolist()],
        n_results=min(top_k, collection.count()),
        include=["documents", "metadatas", "distances"]
    )

    # Convert database results into our existing record format
    matches = []

    for document, metadata, distance in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0]
    ):
        matches.append({
            "source": metadata["source"],
            "section": metadata["section"],
            "chunk_id": metadata["chunk_id"],
            "text": document,
            "similarity": 1 - distance
        })

    return matches



def store_policy_chunks(collection, records: list[dict], embeddings):
    # Make sure the data matches 
    if len(records) != len(embeddings):
        raise ValueError("Records and embeddings must match.")

    if not records:
        return

    # Store the chunks and their metadata
    collection.upsert(
        ids=[
            f"{record['source']}:{record['chunk_id']}"
            for record in records
        ],
        documents=[
            record["text"] for record in records
        ],
        embeddings=embeddings.tolist(),
        metadatas=[
            {
                "source": record["source"],
                "section": record["section"],
                "chunk_id": record["chunk_id"]
            }
            for record in records

        ]
    )

   