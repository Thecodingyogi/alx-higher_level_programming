#!/usr/bin/python3
"""Script that prints the state object with the name passed a argument
    from the database.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == sys.argv[4])
    try:
        print("{}".format(state[0].id))
    except IndexError:
        print("Not found")
