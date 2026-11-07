def add_metadata(chunks: list[str], filename: str) -> list[dict]:
    records = []
     
    for number, chunk in enumerate(chunks, start=1):

        # Use the first line as the section heading
        section = chunk.splitlines()[0]

        # Store the chunk with its source information
        record = {
            "chunk_id": number,
            "source": filename,
            "section": section,
            "text": chunk
        }

        records.append(record)

    return records