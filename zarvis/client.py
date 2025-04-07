from openai import OpenAI

client = OpenAI(
     api_key="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",)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud."},
        {"role": "user", "content": "What is coding?"}
    ]
)

print(completion.choices[0].message.content)
