import openai
import os

def ask_genai(question):
    try:
        client = openai.OpenAI()
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
                {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
            ]
        )

        return completion.choices[0].message
    except Exception as e:
        print(f"General error: {e}")
        return str(e)