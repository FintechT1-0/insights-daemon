from sqlalchemy import Column, Integer, String, Text
from daemon.engine import Base
from pydantic import BaseModel, HttpUrl


class NewsItem(BaseModel):
    url: HttpUrl
    thumbnail: HttpUrl
    image: HttpUrl
    title: str
    content: str
    date: str
    excerpt: str
    lang: str

    class Config:
        from_attributes = True


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, nullable=False)
    thumbnail = Column(String, nullable=False)
    image = Column(String, nullable=False)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    date = Column(String, nullable=False)
    excerpt = Column(Text, nullable=False)
    lang = Column(String, nullable=False)