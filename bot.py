import os
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

API_ID = int(os.environ['API_ID'])
API_HASH = os.environ['API_HASH']
SESSION_STRING = os.environ['SESSION_STRING']

print(f"DEBUG longueur de la session: {len(SESSION_STRING)}")

SOURCE_CHANNEL = -1004382211692
DEST_CHANNELS = ['@chezdh', '@chezz9', '@ChezMendoza']

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)
last_forwarded_id = None

async def main():
    global last_forwarded_id
    await client.start()
    print("Bot démarré. Vérification toutes les 30 minutes...")
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
                print("Pas de nouveau message.")
        await asyncio.sleep(1800)

asyncio.run(main())
