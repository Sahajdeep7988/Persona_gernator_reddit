from config import OPENROUTE_API_KEY, MODELS
from openai import OpenAI

def analyze_demographics(texts):
    prompt = "\n".join(texts)
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=OPENROUTE_API_KEY,
    )
    try:
        result = client.chat.completions.create(
            model=MODELS["demographics"],
            messages=[{"role": "user", "content": prompt}]
        ).choices[0].message.content
        return result
    except Exception as e:
        return f"[ERROR] {str(e)}"
