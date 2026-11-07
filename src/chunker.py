# Finacial Policy AI Assistant 
# Phase 2B: Document Chunking

def chunk_policy(text: str) -> list[str]:
    # Split the document at blank lines
    paragraphs = text.split("\n\n")

    # Store the chunks here
    chunks: list[str] = []

    for paragraph in paragraphs:
        cleaned = paragraph.strip()

        if cleaned:
            chunks.append(cleaned)

    return chunks