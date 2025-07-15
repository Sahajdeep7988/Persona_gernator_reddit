import praw
import logging
from prawcore.exceptions import RequestException, ResponseException, ServerError
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT, REDDIT_USERNAME, REDDIT_PASSWORD
from datetime import datetime
import os
import time

def extract_username_from_url(url):
    if url.endswith('/'):
        url = url[:-1]
    return url.split('/')[-1] if '/user/' in url else None
    
class RedditScraper:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            user_agent=REDDIT_USER_AGENT,
            username=REDDIT_USERNAME,
            password=REDDIT_PASSWORD
        )

    def fetch_reddit_profile_summary(self, username):
        try:
            user = self.reddit.redditor(username)
            profile_info = f"""
--- REDDIT PROFILE SUMMARY ---
Username: {user.name}
Link Karma: {user.link_karma}
Comment Karma: {user.comment_karma}
Total Karma: {user.link_karma + user.comment_karma}
Account Created: {datetime.utcfromtimestamp(user.created_utc).strftime('%Y-%m-%d')}
User Bio: {getattr(user.subreddit, 'public_description', 'Not available')}
------------------------------
"""
            return profile_info.strip()
        except Exception as e:
            return f"Could not retrieve Reddit profile info: {str(e)}"

    def get_user_content(self, username, max_items=100, save_raw=True, output_dir="outputs"):
        user = self.reddit.redditor(username)
        combined = []
        try:
            logging.info("[Scraper] Fetching comments...")
            for comment in user.comments.new(limit=max_items):
                if len(comment.body.strip()) > 30:
                    combined.append(comment.body.strip())

            logging.info("[Scraper] Fetching posts...")
            for post in user.submissions.new(limit=max_items):
                text = post.title + "\n" + (post.selftext or "")
                if len(text.strip()) > 30:
                    combined.append(text.strip())
        except Exception as e:
            logging.error(f"[Scraper] Error fetching data: {e}")

        logging.info(f"[Scraper] Collected {len(combined)} entries")

        # Prepend Reddit profile summary
        profile_summary = self.fetch_reddit_profile_summary(username)
        full_content = profile_summary + "\n\n" + "\n\n".join(combined)

        # Save to raw txt file
        if save_raw:
            os.makedirs(output_dir, exist_ok=True)
            raw_path = os.path.join(output_dir, f"{username}_reddit_raw.txt")
            with open(raw_path, "w", encoding="utf-8") as f:
                f.write(full_content)
            logging.info(f"[Scraper] Raw data saved to {raw_path}")

        return full_content.split("\n\n")
