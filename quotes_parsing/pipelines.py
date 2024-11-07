import os

from sqlalchemy import Column, Integer, String, Text, create_engine
from sqlalchemy.orm import declarative_base, Session

from quotes_parsing.settings import RESULTS_DIR

Base = declarative_base()


class Quote(Base):
    __tablename__ = 'Quote'
    id = Column(Integer, primary_key=True)
    text = Column(Text)
    author = Column(String(200))
    tags = Column(String(400))


class QuotesToDBPipeline:
    def __init__(self):
        RESULTS_DIR.mkdir(exist_ok=True)

    def open_spider(self, spider):
        engine = create_engine(
            f'sqlite:///{os.path.join(RESULTS_DIR, "sqlite.db")}'
        )
        Base.metadata.create_all(engine)
        self.session = Session(engine)

    def process_item(self, item, spider):
        quote = Quote(
            text=item['text'],
            author=item['author'],
            tags=', '.join(item['tags']),
        )
        self.session.add(quote)
        self.session.commit()
        return item

    def close_spider(self, spider):
        self.session.close()
