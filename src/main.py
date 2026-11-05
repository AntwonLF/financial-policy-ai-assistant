from pathlib import Path

# Financial Policy AI Assistant 
# Step 1: Initialize our project

def main(): 
    print("Financial Policy AI Assistant")
    print("Project initialized successfully!")

    data_folder = Path(__file__).resolve().parent.parent / "data"
    print(f"Policy document location: {data_folder}")

if __name__ == "__main__":
    main()
