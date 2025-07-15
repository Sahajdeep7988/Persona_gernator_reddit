import logging
from config import OPENROUTE_API_KEY, MODELS
from openai import OpenAI

def extract_key_quotes(texts):
    prompt = "\n".join(texts)
    logging.info(f"[Quotes] Sending {len(texts)} texts to model {MODELS['quotes']} via OpenRouter...")
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=OPENROUTE_API_KEY,
    )
    try:
        completion = client.chat.completions.create(
            model=MODELS['quotes'],
            messages=[{"role": "user", "content": prompt}]
        )
        result = completion.choices[0].message.content
        logging.info(f"[Quotes] Model replied successfully.")
        return result
    except Exception as e:
        logging.error(f"[Quotes] Model error: {e}")
        return {"error": str(e)}
