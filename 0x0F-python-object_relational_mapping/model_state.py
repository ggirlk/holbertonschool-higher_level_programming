#!/usr/bin/python3
""" model state """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """class state """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                nullable=True, autoincrement=True)
    name = Column(String(50), nullable=False)
