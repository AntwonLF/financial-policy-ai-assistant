
from pathlib import Path
from chunker import chunk_policy


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


if __name__ == "__main__":
    main()
