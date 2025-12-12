from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def call_chatgpt(user_text):
        client = OpenAI()  # # your API key in .env for OpenAI_API_KEY. OpenAI finds key on it s own
    
        response = client.chat.completions.create(
            model="gpt-4o",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": f"Korrigiere den folgenden Text und erkläre, was du wieso geändert hast:\n\n{user_text}"}
            ]
        )
    
        print(f"\033[92m{response.choices[0].message.content}\033[0m")
        print("\n")
        wait = input("Press any key")
        return
