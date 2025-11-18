from apscheduler.schedulers.asyncio import AsyncIOScheduler
from daemon.utils import collect_news
import asyncio

scheduler = AsyncIOScheduler()

scheduler.add_job(collect_news, 'interval', minutes=60*12)

async def main():
    scheduler.start()

    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
