#!/usr/bin/python3
"""Start link class to table in database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from sqlalchemy import table, column
Session = sessionmaker()

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session.configure(bind=engine)
    session = Session()
    newState = State(name="Louisiana")
    session.add(newState)
    session.flush()
    session.refresh(newState)
    print(newState.id)
    session.close()
