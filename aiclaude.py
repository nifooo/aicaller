import os
from dotenv import load_dotenv
from anthropic import Anthropic
from menu import user_text

load_dotenv()

client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")  # gitignore!
)

message = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": f"Korrigiere den folgenden Text:\n\n{user_text}"}
    ]
)

print(message.content[0].text)