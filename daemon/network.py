from daemon.engine import get_async_db
from daemon.models import Article
from daemon.settings import settings
from daemon.config import generate_headers
from loguru import logger
from sqlalchemy import delete
from datetime import datetime
import requests


def send_request(url: str, retry_times: int = 5, include_headers: bool = True) -> str:
    for _ in range(retry_times):
        logger.debug(f"{'proxied' if settings.PROXIED else 'without proxy'}, requesting {url}")
        try:
            if settings.PROXIED:
                resp = requests.get(settings.SCRAPER_API_URL, params={
                    'api_key': settings.SCRAPER_API_KEY,
                    'url': url
                }, timeout=15)
            else:
                if include_headers:
                    resp = requests.get(url, headers=generate_headers(), timeout=15)
                else:
                    resp = requests.get(url, timeout=15)
            resp.raise_for_status()
            return resp.text
        except requests.RequestException as e:
            logger.debug(f"Could not send request: {str(e)}")
            continue
    return ""


async def delete_all_articles():
    async for db in get_async_db():
        try:
            await db.execute(delete(Article))
            await db.commit()
        finally:
            await db.close()
        break


async def save_news_items(news_items: list):
    async for db in get_async_db():
        try:
            for item in news_items:
                db_item = Article(**item)
                db.add(db_item)
            await db.commit()
        finally:
            await db.close()
        break