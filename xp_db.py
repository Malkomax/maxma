'''
This module contains the ORM stuff for the xp/modifiers for the bot
'''
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = sqlalchemy.create_engine('sqlite:///xp.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)

class DiscordUser(Base):
    '''
    This class contains Discord users and tracks their XP.
    '''
    __tablename__ = 'discord_users'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    xp = sqlalchemy.Column(sqlalchemy.Integer)
    def __repr__(self):
        '''
        This is the string rep of a user
        '''
        return f'User {self.id}, {self.xp} XP'

    def provide_modifier(self):
        '''
        this is a stub
        '''
        return self.xp / 3

def make_tables():
    '''
    This method will make all tables in the db.
    '''
    Base.metadata.create_all(engine)

def test():
    '''
    linter suck
    '''
    return 'linters suck'
