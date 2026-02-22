import discord
import os
from dotenv import load_dotenv
import datetime
from datetime import timedelta
import asyncio


load_dotenv()
bot = discord.Bot()

current_time = datetime.datetime.now()
COMPLETION_LOG_CHANNEL_ID = 1475023542784626711


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

    try:
        with open("last_post_date.txt", "r") as f:
            last_post_date = f.read()
            last_post_date = datetime.datetime.fromisoformat(last_post_date)
            difference = current_time - last_post_date
            if difference.days >= 7:
                await create_completion_log(current_time)
            else:
                remaining = timedelta(days=7) - difference
                await asyncio.sleep(remaining.total_seconds())
                await create_completion_log(current_time)
    except FileNotFoundError:
        await create_completion_log(current_time)


async def create_completion_log(time):
    start = time
    end = start + timedelta(days=7)
    title = f"Completion Log {start.strftime('%-m/%-d/%-y')} - {end.strftime('%-m/%-d/%-y')}"
    with open("post.md", "r") as f:
        content = f.read()
    channel = await bot.fetch_channel(COMPLETION_LOG_CHANNEL_ID)
    await channel.create_thread(name=title, content=content)
    with open("last_post_date.txt", "w") as f:
        f.write(time.isoformat())


bot.run(os.getenv("TOKEN"))
