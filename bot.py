!pip install telethon

import asyncio
from telethon import TelegramClient

API_ID = 34452934
API_HASH = "48af12117e408f6f12dac88af5c9a4a9"

SOURCE_CHANNEL = -1004382211692   # ID privé avec préfixe -100
DEST_CHANNELS = ['@chezdh', '@chezz9', '@ChezMendoza']

client = TelegramClient('session_name', API_ID, API_HASH)
last_forwarded_id = None

async def main():
    global last_forwarded_id
    await client.start()
    print("Démarré. Vérification toutes les 30 minutes...")
    while True:
        messages = await client.get_messages(SOURCE_CHANNEL, limit=1)
        if messages:
            latest = messages[0]
            if latest.id != last_forwarded_id:
                for dest in DEST_CHANNELS:
                    await client.forward_messages(dest, latest)
                last_forwarded_id = latest.id
                print(f"Message {latest.id} transféré vers {DEST_CHANNELS}")
            else:
                print("Pas de nouveau message depuis le dernier passage.")
        await asyncio.sleep(1800)  # 30 minutes

await main()
