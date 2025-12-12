from dotenv import load_dotenv
from anthropic import Anthropic


load_dotenv()

def aicaller(user_text):
    client = Anthropic()         # your API key in .env for ANTHROPIC_API_KEY. Anthrophic finds key on it s own
    message = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=1024,
        messages=[
        {"role": "user", "content": f"Korrigiere den folgenden Text:\n\n{user_text}"}
    ]
)

    print(f"\033[92m{message.content[0].text}\033[0m")
    print("\n")
    wait = input("Press any key")
    return