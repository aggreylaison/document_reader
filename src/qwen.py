
from ollama import chat

response = chat(
    model="qwen3:4b",
    messages=[
        {
            "role": "user",
            "content": "Explain what a vector database is in one sentence."
        }
    ]
)

print(response.message.content)