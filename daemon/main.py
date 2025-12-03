from apscheduler.schedulers.asyncio import AsyncIOScheduler
from daemon.utils import collect_news
from daemon.settings import settings
from datetime import datetime
from loguru import logger
import asyncio

scheduler = AsyncIOScheduler()

scheduler.add_job(collect_news, 'interval', minutes=settings.DELAY, next_run_time=datetime.now())

async def main():
    logger.debug("Starting the daemon...")
    scheduler.start()

    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
