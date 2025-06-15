#!/home/qcloud/psngpt/venv/bin/python

import os
import time
import json
from dotenv import load_dotenv
from psnawp_api.psnawp import PSNAWP
from openai import AzureOpenAI
# === Unbuffer stdout for systemd logging ===
import sys
sys.stdout.reconfigure(line_buffering=True)

# === Load environment ===
load_dotenv(dotenv_path="/home/qcloud/psngpt/.env")

# === Config ===
NPSSO_TOKEN = os.getenv("NPSSO_TOKEN")
GROUP_ID = os.getenv("GROUP_ID")
DEPLOYMENT_NAME = os.getenv("AZURE_DEPLOYMENT_NAME")
RESPONDED_FILE = "/app/.replied_storage/.replied_message_uids.json"



# === Azure OpenAI client ===
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version="2024-02-01"
)

def load_replied_uids():
    if not os.path.exists(RESPONDED_FILE):
        with open(RESPONDED_FILE, "w") as f:
            json.dump([], f)
        return []
    with open(RESPONDED_FILE, "r") as f:
        return json.load(f)

def save_replied_uids(uids):
    with open(RESPONDED_FILE, "w") as f:
        json.dump(uids, f)

def is_ai_prompt(text: str) -> bool:
    return text.strip().lower().startswith("ai ")

def get_prompt_body(text: str) -> str:
    return text[3:].strip()

def get_ai_reply(prompt: str) -> str:
    system_prompt = (
"You are a witty, street-smart AI assistant living inside a PlayStation Network group chat. "
        "Speak casually. Keep replies short, funny, and sharp. "
                "You give real gaming tips, roast players, generate memes, and jump into convos like one of the squad. "
                        "You have full knowledge of Black Ops 6 2024 weapons, stats, attachments, and meta builds. "
                                "Use this to settle arguments, suggest loadouts, or call out bad setups. "
                                        "Never be formal. Never act like a generic assistant. Always sound like part of the crew."
                                            
)
    try:
        response = client.chat.completions.create(
            model=DEPLOYMENT_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("❌ GPT error:", e)
        return "yo chill, gimme a sec 😅"

def main():
    psnawp = PSNAWP(NPSSO_TOKEN)
    group = psnawp.group(group_id=GROUP_ID)
    replied_uids = load_replied_uids()

    print("✅ PSN GPT bot started...")

    while True:
        try:
            conversation = group.get_conversation(10)
            messages = conversation["messages"]

            for message in messages:
                message_id = message["messageUid"]
                body = message["body"].strip()
                author = message["sender"]["onlineId"]

                # Skip if already replied to this UID
                if message_id in replied_uids:
                    continue

                # Only respond to messages starting with "ai"
                if is_ai_prompt(body):
                    prompt = get_prompt_body(body)
                    print(f"👤 {author}: {prompt}")
                    reply = get_ai_reply(prompt)
                    print(f"🤖 GPT: {reply}")
                    group.send_message(reply)

                # Always log the UID, even if not a prompt, so we never reprocess
                replied_uids.append(message_id)

            # Keep memory to last 100 UIDs
            save_replied_uids(replied_uids[-100:])
            time.sleep(20)

        except Exception as e:
            print("⚠️ Error polling group:", e)
            time.sleep(30)

if __name__ == "__main__":
    main()

