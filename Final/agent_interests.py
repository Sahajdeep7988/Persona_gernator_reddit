from config import OPENROUTE_API_KEY, MODELS
from openai import OpenAI

def analyze_interests(texts):
    prompt = "\n".join(texts)
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=OPENROUTE_API_KEY,
    )
    completion = client.chat.completions.create(
        model=MODELS["interests"],
        messages=[{"role": "user", "content": prompt}]
    )
    result = completion.choices[0].message.content
    return result