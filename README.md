# 🕹️ PSN GPT Bot

This bot brings ChatGPT (via Azure OpenAI) directly into your PlayStation Network (PSN) group chat. It listens for messages that begin with `ai ` and responds with witty, sharp, and in-character replies—like a squadmate with gaming wisdom and roasts.

---

## 🧠 What It Does

- Listens to your PSN group chat messages.
- Detects if a message starts with `ai `.
- Sends the rest of the message to ChatGPT (via Azure OpenAI).
- Responds back in the PSN chat with a short, funny, street-smart reply.
- Remembers which messages it has replied to, so it doesn't respond twice.

---

## 📦 Project Structure

```
psn-gpt/
├── psn-gpt.py                  # Main script
├── requirements.txt            # Python dependencies
├── Dockerfile                  # For containerization
└── .replied_storage/           # Mounted volume for message tracking
    └── .replied_message_uids.json
```

---

## 🛠 Environment Variables

Make sure to configure the following:

| Variable Name           | Description                          |
|------------------------|--------------------------------------|
| `NPSSO_TOKEN`          | Your PSN session token               |
| `GROUP_ID`             | PSN Group Chat ID                    |
| `AZURE_OPENAI_API_KEY` | Azure API key for ChatGPT            |
| `AZURE_OPENAI_ENDPOINT`| Your Azure OpenAI endpoint URL       |
| `AZURE_DEPLOYMENT_NAME`| Deployment name (e.g., `gpt-4o`)     |

---

## 🚀 Deploy with Coolify

1. Push this repo to GitHub.
2. Go to Coolify → **New App → Git Repository**
3. Configure:
   - Dockerfile Path: `Dockerfile`
   - Volume Mount:
     - Destination: `/app/.replied_storage`
     - Source: `/data/psn-gpt-replies` (or similar)
4. Set required environment variables.
5. Click **Deploy Now**.

---

## 🧪 Local Development

```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python psn-gpt.py
```

Make sure your `.env` file includes all required environment variables listed above.

---

## 💬 Example Usage

> **Player:** `ai what's the best SMG in BO6 right now?`  
> **Bot:** *Try the Striker 9 with Rapidfire and 40-round mag—unless you're tryna get clapped 😤*

---

## 🙏 Credits

- [PSNAWP](https://github.com/benjimaw/psnawp) — PSN access via web APIs
- [Azure OpenAI](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/) — for GPT chat power
- [Coolify](https://coolify.io) — deploy with ease

