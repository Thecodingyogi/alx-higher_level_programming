#!/usr/bin/python3
"""Script that prints all states with the letter 'a'"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id)\
            .filter(State.name.like('%a%')):
        print("{}: {}".format(state.id, state.name))
