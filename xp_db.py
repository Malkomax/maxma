import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = sqlalchemy.create_engine('sqlite:///xp.db')

Base = declarative_base()

class discordUser(Base):
    __tablename__ = 'discord_users'
    id = Column(Integer, primary_key=True)
    xp = Column(Integer)

    def __repr__(self):
        return f'User {self.id}, {self.xp} XP'

Session = sessionmaker(bind=engine)

def make_tables():
    Base.metadata.create_all(engine)
