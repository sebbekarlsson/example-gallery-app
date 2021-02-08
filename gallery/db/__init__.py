from sqlalchemy import (
    create_engine, Column, Integer, String, MetaData, Table
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine(
    'mysql+pymysql://guest:abc123@localhost/gallery', echo=True
)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


class Image(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True)
    filename = Column(String(300))
    title = Column(String(300))


def create_image(filename, title):
    img = Image(filename=filename, title=title)
    session.add(img)
    session.commit()
    return img


def get_images():
    return session.query(Image)


if not engine.dialect.has_table(engine, 'images'):
    metadata = MetaData(engine)
    Table(
        'images', metadata,
        Column('Id', Integer, primary_key=True, nullable=False),
        Column('filename', String(300)), Column('title', String(300))
    )
    metadata.create_all()
