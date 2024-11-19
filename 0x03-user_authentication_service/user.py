#!/usr/bin/env python3
"""this module for creating alchym user model"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
Base = declarative_base()


class User(Base):
    """
    create table
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)\


    def __repr__(self):
        """class to present the table"""
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name, self.fullname, self.nickname)


engine = create_engine('sqlite:///users.db', echo=True)
Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()
