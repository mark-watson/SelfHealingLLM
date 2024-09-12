import os
import time
import anthropic

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
client = anthropic.Client(api_key=ANTHROPIC_API_KEY)


def send_claude_request(prompt: str) -> str:
    response = message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=500,
        messages=[{
            "role":
            "user",
            "content":
            f"{anthropic.HUMAN_PROMPT} {prompt}{anthropic.AI_PROMPT}"
        }])
    print(message.content[0].text)
    return message.content[0].text.strip()
