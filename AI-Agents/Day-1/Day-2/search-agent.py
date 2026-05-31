import anthropic

client = anthropic.Anthropic()  # uses ANTHROPIC_API_KEY env var

def search_agent(query: str) -> str:
    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        tools=[{"type": "web_search_20250305", "name": "web_search"}],
        messages=[{"role": "user", "content": query}],
    )

    # Extract text from response content blocks
    return "\n".join(
        block.text for block in response.content if hasattr(block, "text")
    )


if __name__ == "__main__":
    result = search_agent("What is the latest news in AI today?")
    print(result)