from daemon.config import CATEGORY_LABELS
import random


# frozen until better times...
async def classify_text(html: str, lang: str) -> str:
    return random.choice(CATEGORY_LABELS)