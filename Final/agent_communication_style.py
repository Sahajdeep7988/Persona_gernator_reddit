from config import OPENROUTE_API_KEY, MODELS
from openai import OpenAI

def analyze_communication_style(texts):
    prompt = "\n".join(texts)
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=OPENROUTE_API_KEY,
    )
    completion = client.chat.completions.create(
        model=MODELS["communication"],
        messages=[{"role": "user", "content": f"Analyze the following Reddit posts for communication style. Be concise.\n{texts}"}],
        max_tokens=512,
    )
    result = completion.choices[0].message.content
    return result
