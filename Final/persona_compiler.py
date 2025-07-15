import logging
import os
from config import OPENROUTE_API_KEY, MODELS
from openai import OpenAI

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize OpenAI client
client = OpenAI(api_key=OPENROUTE_API_KEY, base_url="https://openrouter.ai/api/v1")

def read_file(path):
    """Reads a file and returns its content as a string."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return ""


def compile_persona(demo_txt, comm_txt, int_txt, tech_txt, quotes_txt):
    """Compiles a detailed persona using model responses and a strict prompt."""
    # Persona prompt template
    prompt = f"""
You are a professional behavioral analyst. Your job is to extract a detailed, strictly formatted user persona from the following model outputs.
IMPORTANT: Output must be in plain text only. Do NOT use Markdown formatting (no **, *, #, or ---). Use only simple text, dashes, and colons for structure.
STRICT RULES:
- Your output must ONLY be the persona structure below, with NO explanations, NO notes, NO introductory or summary text, and NO extra lines before or after. Do not include any sentences like 'Below is the persona...', 'Here is the filled template as per your instructions:', 'Note: ...', or any other commentary. Only output the structure and its content, nothing else.
- For any attribute that cannot be strictly confirmed, provide a reasoned guess, but clearly mark it as a guess and state the basis for the guess (e.g., 'Not confirmed, but likely X based on [evidence]').
- Do not hallucinate or add extra information not supported by the model outputs.
- For 'Quote Highlights' and 'Citations', include as many relevant points as the evidence supports (not just two). The template is a guide, not a limit.
- Be strict, concise, and professional. Use the following template and fill in as much as possible:

Name: [Generated name or "Not confirmed"]

Demographics:
- Age:
- Location:
- Gender:
- Occupation:

Behavioral Traits:
- Communication Style:
- Online Behavior:
- Posting Frequency:
- Preferred Topics:

Psychographic Profile:
- Interests / Hobbies:
- Values:
- Motivations:
- Frustrations:

Technology Usage:
- Devices Used:
- Platforms Used Outside of Reddit:
- Tech Proficiency:

Quote Highlights:
- [List as many as are relevant, one per line]

Citations:
- [List as many as are relevant, one per line]

MODEL OUTPUTS:
Demographics:
{demo_txt}

Communication:
{comm_txt}

Interests:
{int_txt}

Technology:
{tech_txt}

Quotes:
{quotes_txt}
"""

    try:
        completion = client.chat.completions.create(
            model=MODELS['compiler'],
            messages=[{"role": "user", "content": prompt}]
        )
        result = completion.choices[0].message.content
        # Remove all '**' from the output
        result = result.replace('**', '')
        return result
    except Exception as e:
        logging.error(f"[Compiler] Model error: {e}")
        return "[ERROR] Persona compilation failed."

def save_persona_to_txt(persona_text, filename):
    """Saves compiled persona to a .txt file."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(persona_text)
        logging.info(f"Persona saved to {filename}")
    except Exception as e:
        logging.error(f"Failed to save persona: {e}")
