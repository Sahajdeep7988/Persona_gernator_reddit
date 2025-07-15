
---

# Reddit Persona Generator

A modular, production-grade system that generates deeply structured user personas from public Reddit profiles using open-source LLMs. Designed for behavioral analysis, LLM fine-tuning, and psychographic research pipelines.

Powered entirely by free APIs and built to support future enhancements like parallel agent orchestration and dynamic scraping agents.

---

## 🔍 What It Does

This tool scrapes Reddit posts and comments from any public user profile, passes the raw data through multiple specialized AI agents (each focused on different psychological/behavioral dimensions), and then compiles everything into a clean, professionally formatted persona document.

---

## 🧠 Features

* **Agent-based architecture:** Each agent focuses on one core trait group (e.g. demographics, communication, interests).
* **Open-source LLMs via OpenRouter:** No vendor lock-in, and no reliance on closed commercial APIs.
* **Structured persona generation:** Final output is plain text (no Markdown), designed for readability and integration.
* **CLI-based execution:** One command to extract + analyze + generate persona.
* **Future-proof:** Easily extendable for new agents, parallel processing, or external scraping tasks.
* **Ethically conscious:** Only uses publicly available content. No scraping of private messages.

---

## 🗂️ Project Structure

```
Reddit_Persona_Generator/
├── Final/
│   ├── agent_communication_style.py     # Extracts tone, patterns, and language use
│   ├── agent_demographics.py            # Guesses age, gender, job, and location
│   ├── agent_interests.py               # Identifies hobbies, passions, communities
│   ├── agent_technology_usage.py        # Detects device habits and tech stack mentions
│   ├── agent_quotes.py                  # Pulls high-signal quotes from content
│   ├── persona_compiler.py              # Merges agent outputs into structured persona
│   ├── reddit_scraper.py                # Fetches posts/comments from Reddit via PRAW
│   ├── config.py                        # API keys and model configurations
│   └── main.py                          # Orchestration script
├── outputs/                             # Stores final personas + raw Reddit data
├── requirements.txt
├── .env                                 # Your API keys (excluded from git)
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Sahajdeep7988/Persona_gernator_reddit.git
cd Reddit_Persona_Generator
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file inside the `Final/` folder with the following:

```dotenv
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=your_user_agent
REDDIT_USERNAME=your_reddit_username
REDDIT_PASSWORD=your_reddit_password
OPENROUTE_API_KEY=your_openrouter_api_key
```

> 🔑 [Get Reddit API keys](https://www.reddit.com/prefs/apps)
> 🌐 [Get an OpenRouter API key](https://openrouter.ai/)

---

## 🚀 Usage

To generate a persona:

```bash
python Final/main.py "https://www.reddit.com/user/<username>/"
```

* The system will:

  1. Scrape the user's profile
  2. Analyze it via five agents
  3. Compile a clean text persona to `outputs/<username>_persona.txt`

---

## 🧪 Sample Output (truncated)

```
Name: Spez (Steve Huffman)

Demographics:
- Age: Possibly mid-30s based on long references to career, startups, and Reddit tenure
- Gender: Male (inferred from post phrasing and pronouns used)
- Location: Likely US-based (mentions of California, SF)
- Occupation: Tech executive or founder (confirmed via post in r/startups)

...

Quote Highlights:
- “Reddit works because it’s human.”
- “I still remember launching the first version of this feature 7 years ago.”

Citations:
- Occupation from: “As CEO of Reddit, I’ve seen the platform evolve...”
- Location from: “When I moved to San Francisco, I knew...”
```

---

## ⚖️ Ethical Disclaimer

* All data is scraped from **publicly available Reddit profiles**.
* This project is **not affiliated with Reddit** and adheres to Reddit's API TOS.
* We **do not claim the generated personas are 100% accurate.** They are inferred through LLMs and should be interpreted as such.
* If your Reddit profile is referenced and you wish to opt out, contact the maintainer below.

---

## 📌 Maintainer

**Sahajdeep Singh**

Email: [sahajdeepsingh404@gmail.com](mailto:sahajdeepsingh404@gmail.com)

---

## 🧭 Future Enhancements

* 🔁 **Parallel Agent Execution**
  Currently sequential due to free API rate limits (60 RPM). Easily extendable using threading or asyncio for faster runtime with premium keys.

* 🌍 **Link-Aware Enrichment (v2 planned)**
  A “second brain” agent can detect GitHub/LinkedIn links in content and enrich the persona with confirmed attributes.

* 🕸️ **LLM-directed Scraper Agent**
  Future: LLM tells scraper what to look for (e.g., “find their portfolio”), allowing richer inputs for future model runs.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---