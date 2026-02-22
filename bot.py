import discord
import os
from dotenv import load_dotenv
import datetime
from datetime import timedelta
import asyncio


load_dotenv()
bot = discord.Bot()

COMPLETION_LOG_CHANNEL_ID = 1475023542784626711
LAST_POST_DATE_FILE = "last_post_date.txt"
POST_INTERVAL = timedelta(days=7)


def get_last_post_date():
    try:
        with open(LAST_POST_DATE_FILE, "r") as f:
            last_post_date = f.read().strip()
            if not last_post_date:
                return None
            return datetime.datetime.fromisoformat(last_post_date)
    except FileNotFoundError:
        return None


def update_last_post_date(date_time):
    with open(LAST_POST_DATE_FILE, "w") as f:
        f.write(date_time.isoformat())


async def create_completion_log(post_time):
    end = post_time + POST_INTERVAL
    title = f"Completion Log {post_time.strftime('%-m/%-d/%-y')} - {end.strftime('%-m/%-d/%-y')}"
    with open("post.md", "r") as f:
        content = f.read()
    channel = await bot.fetch_channel(COMPLETION_LOG_CHANNEL_ID)
    # this assert is to narrow the type for the LSP so it doesn't show an error
    assert isinstance(channel, discord.ForumChannel)
    await channel.create_thread(name=title, content=content)
    update_last_post_date(post_time)


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    last_post_date = get_last_post_date()

    if last_post_date is not None:
        elapsed_time = datetime.datetime.now() - last_post_date
        remaining_time = POST_INTERVAL - elapsed_time
        if remaining_time.total_seconds() > 0:
            await asyncio.sleep(remaining_time.total_seconds())

    await create_completion_log(datetime.datetime.now())


bot.run(os.getenv("TOKEN"))
