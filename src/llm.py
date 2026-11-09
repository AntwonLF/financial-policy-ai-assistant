# Financial Policy AI Assistant
# Phase 4: LLM Integration

from ollama import chat

def generate_answer(prompt: str) -> str:

    # Send our prepared prompt to the local LLM
    response = chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt

            }
        ]
    )

    # Extract the generated answer 
    return response.message.content