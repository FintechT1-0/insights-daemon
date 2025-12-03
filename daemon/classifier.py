from transformers import pipeline
from bs4 import BeautifulSoup
from daemon.config import CATEGORY_LABELS
from googletrans import Translator
from loguru import logger


classifier = pipeline("zero-shot-classification",
                      model="joeddav/xlm-roberta-large-xnli")


translator = Translator()


async def translate(text: str, source: str = 'uk', destination: str = 'en') -> str:
    try:
        translation = await translator.translate(text, src=source, dest=destination)
        logger.debug(f"Translated '{text}' as '{translation.text}")
        return translation.text
    except Exception as e:
        logger.debug(f"Error while translating: {str(e)}")
        return text


def html_to_text(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text(separator="\n", strip=True)


async def classify_text(html: str, lang: str) -> str:
    text = html_to_text(html)
    if lang == 'ua':
        text = await translate(text)

    result = classifier(html_to_text(html), CATEGORY_LABELS)
    return result["labels"][0]
