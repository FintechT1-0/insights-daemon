from sqlalchemy import Column, Integer, String, Text
from daemon.engine import Base
from pydantic import BaseModel, HttpUrl, Field


class NewsItem(BaseModel):
    url: HttpUrl
    thumbnail: HttpUrl
    image: HttpUrl
    title: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)
    date: str = Field(..., min_length=1)
    excerpt: str = Field(..., min_length=1)
    lang: str = Field(..., min_length=1)

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
    category = Column(String, nullable=False)