import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("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"))

print("AI chatbot running on Render... type exit to quit.\n")

while True:
    user = input("You: ")
    if user.lower() == "exit":
        break

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user}]
    )

    print("Bot:", res.choices[0].message.content)
