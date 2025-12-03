from daemon.models import NewsItem
from pydantic import ValidationError
from loguru import logger
from datetime import datetime
from daemon.scraping import get_daily_news_EN, get_daily_news_UA
from daemon.network import delete_all_articles, save_news_items
from daemon.classifier import classify_text
import gc


def validate_items(raw_items: list[dict]) -> list[NewsItem]:
    validated = []
    for item in raw_items:
        try:
            news_item = NewsItem(**item)
            validated.append(item)
        except ValidationError:
            continue
    return validated


async def collect_news():
    logger.debug(f"Trying to collect news at {datetime.utcnow()}")

    validated_EN = validate_items(get_daily_news_EN())
    validated_UA = validate_items(get_daily_news_UA())

    if len(validated_EN) < 5 or len(validated_UA) < 5:
        logger.debug(f"Not enough news to renew: {len(validated_EN)} for EN and {len(validated_UA)} for UA")

    else:
        for item in validated_EN:
            item["category"] = await classify_text(item["title"] + "\n" + item["excerpt"], "en")

        for item in validated_UA:
            item["category"] = await classify_text(item["title"] + "\n" + item["excerpt"], "ua")
            
        await delete_all_articles()
        await save_news_items(validated_EN + validated_UA)

        logger.debug(f"Updated and saved news sucessfully")
    
    gc.collect()


