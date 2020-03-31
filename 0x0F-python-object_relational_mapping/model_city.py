#!/usr/bin/python3
""" model City """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from model_state import Base, State


class City(Base):
    """class City """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False,
                      ForeignKey('states.id'))
