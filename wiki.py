import asyncio
import aiohttp
import json
import os
from dotenv import load_dotenv
from aiohttp import ClientSession
from urllib.parse import quote

# Load secrets
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Load config
with open("config.json") as f:
    config = json.load(f)

TOPICS_FILE = config.get("topics_file", "topics.txt")
CONCURRENCY = config.get("concurrency", 10)
MAX_RETRIES = config.get("max_retries", 3)
TELEGRAM_ENABLED = config.get("telegram_enabled", True)


async def send_telegram_message(message: str):
    if not TELEGRAM_ENABLED:
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload, timeout=10) as response:
                if response.status != 200:
                    print(f"Telegram failed: {await response.text()}")
    except Exception as e:
        print(f"Telegram error: {e}")


async def fetch_topic(session: ClientSession, topic: str):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{quote(topic)}"
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            async with session.get(url, timeout=10) as response:
                if response.status == 200:
                    data = await response.json()
                    title = data.get("title", "No Title")
                    extract = data.get("extract", "No summary available.")
                    page_url = data.get("content_urls", {}).get("desktop", {}).get("page", "")

                    msg = f"✅ *Topic:* {title}\n📄 *Summary:* {extract}\n🔗 {page_url}"
                    await send_telegram_message(msg)
                    print(f"✅ Fetched: {topic}")
                    return
                elif response.status == 404:
                    print(f"❌ Not found: {topic}")
                    return
        except Exception as e:
            print(f"[Retry {attempt}/{MAX_RETRIES}] Exception for {topic}: {e}")
    print(f"❌ Failed to fetch {topic}")


async def main():
    with open(TOPICS_FILE, "r", encoding="utf-8") as f:
        topics = [line.strip() for line in f if line.strip()]

    connector = aiohttp.TCPConnector(limit=None)
    timeout = aiohttp.ClientTimeout(total=30)

    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        sem = asyncio.Semaphore(CONCURRENCY)
        tasks = []

        async def bound_fetch(topic):
            async with sem:
                await fetch_topic(session, topic)

        for topic in topics:
            tasks.append(bound_fetch(topic))

        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())