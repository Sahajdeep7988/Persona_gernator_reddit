from config import OPENROUTE_API_KEY, MODELS
from openai import OpenAI

def analyze_technology_usage(texts):
    prompt = "\n".join(texts)
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=OPENROUTE_API_KEY,
    )
    completion = client.chat.completions.create(
        model=MODELS["technology"],
        messages=[{"role": "user", "content": f"Analyze the following Reddit posts for technology usage. Be concise.\n{texts}"}],
        max_tokens=512,
    )
    result = completion.choices[0].message.content
    return result
