#!/usr/bin/python3
"""
fetch first state
"""
import sys

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = sys.argv[4]

    instances = len(session.query(State).filter_by(state))
    if instances == 0:
        print("Not found")
    else:
        print(instances)
