
import os
from telethon import TelegramClient, events
from pushbullet import Pushbullet

# Load environment variables
api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
phone = os.getenv('PHONE_NUMBER')
pushbullet_token = os.getenv('PUSHBULLET_TOKEN')

# Set keywords to filter
keywords = ["AI", "AI agent"]

# Initialize Pushbullet
pb = Pushbullet(pushbullet_token)

# Function to send push notification
def send_push_notification(message):
    pb.push_note("Telegram Alert", message)

# Initialize Telegram client
client = TelegramClient('session_name', api_id, api_hash)

# Connect and sign in if needed
async def main():
    await client.start(phone=phone)
    print("Client is running...")

@client.on(events.NewMessage)
async def handler(event):
    message_text = event.message.message
    if any(keyword.lower() in message_text.lower() for keyword in keywords):
        print(f"Matched: {message_text}")
        send_push_notification(message_text)

with client:
    client.loop.run_until_complete(main())
    client.run_until_disconnected()
