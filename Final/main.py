import os
import sys
import argparse
import logging
from reddit_scraper import RedditScraper, extract_username_from_url
from agent_demographics import analyze_demographics
from agent_communication_style import analyze_communication_style
from agent_interests import analyze_interests
from agent_technology_usage import analyze_technology_usage
from agent_quotes import extract_key_quotes
from persona_compiler import compile_persona, save_persona_to_txt


def main():
    if len(sys.argv) != 2:
        print("Usage: python Final/main.py <reddit_profile_url>")
        return

    profile_url = sys.argv[1]
    username = extract_username_from_url(profile_url)
    if not username:
        logging.error("Invalid Reddit profile URL.")
        print("[ERROR] Invalid Reddit profile URL.")
        return

    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"{username}_persona.txt")

    scraper = RedditScraper()
    texts = scraper.get_user_content(username)
    # Fallback: check for scraping errors or missing user
    if not texts or (len(texts) == 1 and texts[0].startswith('Could not retrieve Reddit profile info')):
        logging.error(f"Reddit user '{username}' not found or could not be scraped. Exiting.")
        print(f"[ERROR] Reddit user '{username}' not found or could not be scraped. Exiting.")
        return

    demo_txt = analyze_demographics(texts)
    comm_txt = analyze_communication_style(texts)
    int_txt = analyze_interests(texts)
    tech_txt = analyze_technology_usage(texts)
    quotes_txt = extract_key_quotes(texts)

    persona_text = compile_persona(
        demo_txt,
        comm_txt,
        int_txt,
        tech_txt,
        quotes_txt
    )
    save_persona_to_txt(persona_text, output_file)
    print(f"Persona file saved: {output_file}")

if __name__ == "__main__":
    main()
