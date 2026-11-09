
from pathlib import Path

from .chunker import chunk_policy
from .metadata import add_metadata
from .embeddings import generate_embeddings
from .search import search_policies
from .context import build_context
from .prompts import build_prompt
from .llm import generate_answer



# Financial Policy AI Assistant
# Phase 2: Loading banking policy documents


def main():
    print("Financial Policy AI Assistant")
    print("Project initialized successfully!")

    # Step 1: Find our data folder
    data_folder = Path(__file__).resolve().parent.parent / "data"
    print(f"Policy document location: {data_folder}")

    # Step 2: Locate the banking policy
    policy_file = data_folder / "access_control_policy.txt"

    # Step 3: Check if the file exists
    if not policy_file.exists():
        print("Error: Policy document not found!")
        return

    # Step 4: Read the policy
    policy_text = policy_file.read_text(encoding="utf-8")

    # Step 5: Display the contents
    print("\n--- Loaded Banking Policy ---")
    print(policy_text)

    # Split the loaded policy into smaller chunks
    chunks = chunk_policy(policy_text)

    #  Display the total number of chunks 
    print(f"\nCreated {len(chunks)} chunks:")

    # Display each chunk individually
    for number, chunk in enumerate(chunks, start=1):
        print(f"\n--- Chunk {number} ---")
        print(chunk)    

    # Add source metadata to each chunk
    records = add_metadata(chunks, policy_file.name)

    print("\n--- Document Metadata ---")

    for record in records:
        print(f"\nChunk ID: {record['chunk_id']}")
        print(f"Source: {record['source']}")
        print(f"Section: {record['section']}")

    # Phase 3: Generate embeddings for policy chunks
    print("\n--- Gener?ating Embeddings ---")

    embeddings = generate_embeddings(chunks)

    print("Embeddings generated successfully!")
    print(f"Number of  chunks: {len(embeddings)}")
    print(f"Dimensions per embedding: {embeddings.shape[1]}")
    print(f"Embedding array shape: {embeddings.shape}")

       # Examine an actual embedding
    print("\n--- Exploring Embeddings ---")

    print("First five numerical values:")
    print(embeddings[0][:5])

    # Compare two different policy sections
    similarity = embeddings[2] @ embeddings[3]

    print(f"Employee Access vs MFA similarity: {similarity:.3f}")

    
    # Phase 3: Search banking policies by meaning
    print("\n--- Semantic Policy Search ---")

    question = "How quickly must employees access be removed after termination?"

    results = search_policies(question, records, embeddings, top_k=3)

    print(f"\nQuestion: {question}")

    for result in results:
        print(f"\nSection: {result['section']}")
        print(f"Source: {result['source']}")
        print(f"Similarity: {result['similarity']:.3f}")
        print(f"Policy: {result['text']}")

    # Phase 4: Prepare restrieved evidence for the LLM
    print('\n--- LLM Context ---')

    context = build_context(results)

    print(context)

    # Phase 4: Build the prompt for the LLM
    print("\n--- LLM Prompt ---")

    prompt = build_prompt(question, context)

    print(prompt)

   
    # Generate an AI response from the policy evidence
    print("\n--- AI Generated Answer ---")

    answer = generate_answer(prompt)

    print(answer)




if __name__ == "__main__":
    main()
