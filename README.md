# 🎮 PSN AI Bot

This is an automated PlayStation Network (PSN) monitoring bot that uses the PSNAWP API and Azure OpenAI to:

- Detect when **clan members** or **founders** are online.
- Generate **DALL·E 3 images** of active players as comic characters.
- Send **alerts to Discord** with custom visuals.
- Drop **AI-powered hype messages** in PSN group chat when certain players are online together.

---

## 🛠 Features

- ✅ Real-time PSN status check (via `psnawp`)
- ✅ Discord webhook alert with image generation (DALL·E 3)
- ✅ Hype message drop using Azure GPT-4o
- ✅ JSON state tracking to avoid spammy alerts
- ✅ Fully Dockerized & deployable on [Coolify](https://coolify.io)

---

## 📦 Project Structure

```
psn-alert/
├── psn-gpt.py                    # Main script
├── requirements.txt             # Python dependencies
├── Dockerfile                   # For containerization
├── .dockerignore                # Build exclusions
```

---

## 🚀 Deploy with Coolify

1. Push code to GitHub
2. On Coolify:
   - Select **"New App → Git Repository"**
   - Choose this repo
   - Set Dockerfile path to `Dockerfile`
   - Add a **volume mount**:
     - Destination: `/app/alert_data`
     - Source: `/data/psn-alert-data` or similar
3. Set the following **environment variables**:

| Variable Name                 | Description                                    |
|------------------------------|------------------------------------------------|
| `NPSSO_TOKEN`                | Your PSN auth token                            |
| `DISCORD_WEBHOOK`           | Discord Webhook URL for alerts                 |
| `GPT_AZURE_OPENAI_API_KEY`  | GPT API Key for Azure OpenAI (chat)            |
| `GPT_AZURE_OPENAI_ENDPOINT` | GPT API Endpoint (chat)                        |
| `GPT_AZURE_DEPLOYMENT_NAME` | GPT deployment name (e.g., `gpt-4o`)           |
| `AZURE_OPENAI_API_KEY`      | API Key for DALL·E 3 image generation          |
| `AZURE_OPENAI_ENDPOINT`     | Endpoint for DALL·E 3                          |

4. Click **Deploy Now**

---

## 🧠 AI Prompting Logic

- Players are mapped to prompt fragments (e.g., "a gamer with a soup can helmet")
- When 2+ are online, a full DALL·E 3 prompt is generated with comic-style descriptions
- GPT-4o generates short meme-style messages for in-game chat when a hype moment triggers

---

## 🔒 State Tracking

Uses two JSON files:
- `.last_founder_alert.json`
- `.last_clan_alert.json`

These are stored in `/app/alert_data` (mapped to a persistent volume) to track who was last online, preventing repeated alerts.

---

## 🧪 Local Development

```bash
# Run locally
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python psn-ai.py
```

Create a `.env` file (or set environment variables directly).

---

## 📸 Example Alert

> 🟢 Founders Online Alert: BrendanSoup, ASamad89, mutasif  
> *(Image of comic-style characters sent to Discord)*

---

## 🙏 Credits

- [PSNAWP API](https://github.com/benjimaw/psnawp) for PSN access
- [Azure OpenAI](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/) for GPT & DALL·E
- [Coolify](https://coolify.io) for self-hosted deployment magic

