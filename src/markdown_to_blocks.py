def markdown_to_blocks(markdown):
    return list(
        filter(
            lambda b: b != "",
            map(
                lambda b: b.strip(),
                markdown.split("\n\n")
            )
        )
    )
    
