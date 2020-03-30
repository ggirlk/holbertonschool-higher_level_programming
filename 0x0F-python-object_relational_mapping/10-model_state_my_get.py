#!/usr/bin/python3
"""Start link class to table in database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
Session = sessionmaker()

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session.configure(bind=engine)
    session = Session()
    k = 0
    for state in session.query(State).filter(State.name == argv[4]):
        k = 1
        print("{}".format(state.id))
    if k == 0:
        print("Not found")
    session.close()
