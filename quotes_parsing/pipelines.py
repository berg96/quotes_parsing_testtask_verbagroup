import os

from sqlalchemy import (
    Column, Integer, String, Text, UniqueConstraint, create_engine
)
from sqlalchemy.orm import Session, declarative_base

from quotes_parsing.settings import RESULTS_DIR

Base = declarative_base()


class Quote(Base):
    __tablename__ = 'Quote'
    id = Column(Integer, primary_key=True)
    text = Column(Text)
    author = Column(String(200))
    tags = Column(String(400))

    __table_args__ = (
        UniqueConstraint('text', 'author', name='unique_text_author'),
    )


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
        if not self.session.query(Quote).filter_by(
                text=item['text'], author=item['author']
        ).first():
            self.session.add(Quote(
                text=item['text'],
                author=item['author'],
                tags=', '.join(item['tags']),
            ))
            self.session.commit()
        return item

    def close_spider(self, spider):
        self.session.close()
