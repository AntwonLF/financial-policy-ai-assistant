
# Financial Policy AI Assistant
# Phase 4: Prepare policy context for the LLM


def build_context(results: list[dict]) -> str:

    # Handle searches with no results
    if not results:
        return "No relevant policy sections were retrieved."

    context_blocks = []

    # Organize each retrieved policy section
    for result in results:
        block = (
            f"Source: {result['source']}\n"
            f"Section: {result['section']}\n"
            f"Policy Text: {result['text']}"
        )

        context_blocks.append(block)

    # Combine the sections into one context string
    return "\n\n---\n\n".join(context_blocks)
