import os
import time
from openai import OpenAI

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai_client = OpenAI(api_key=OPENAI_API_KEY)


def send_openai_request(prompt: str) -> str:
    completion = openai_client.chat.completions.create(model="gpt-4o-mini",
                                                       messages=[{
                                                           "role":
                                                           "user",
                                                           "content":
                                                           prompt
                                                       }],
                                                       max_tokens=500)
    print(completion)
    content = completion.choices[0].message.content
    print(f"\n\n* content:\n{content}\n\n")
    return content
