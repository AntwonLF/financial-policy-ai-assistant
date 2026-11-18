from pathlib import Path

from .chunker import chunk_policy
from .metadata import add_metadata
from .embeddings import generate_embeddings
from .database import get_policy_collection, store_policy_chunks

def main():
    # Locate and read our fiticionalm banking policy document
    policy_file = (
        Path(__file__).resolve().parent.parent 
        / "data" 
        / "access_control_policy.txt"
    )

    policy_text = policy_file.read_text(encoding="utf-8")

    # Prepare the document for storage 
    chunks = chunk_policy(policy_text)
    records = add_metadata(chunks, policy_file.name)
    embeddings = generate_embeddings(chunks)

    # Save everything to ChromaDB
    collection = get_policy_collection()
    store_policy_chunks(collection, records, embeddings)

    print(f"Stored chunks: {collection.count()}")

if __name__ == "__main__":
    main()
