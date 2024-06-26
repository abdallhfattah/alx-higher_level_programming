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
    instances = session.query(State).filter(
        State.name == (state,)).order_by(State.id).all()
    if instances:
        print(instances[0].id)
    else:
        print("Not found")
    session.close()
