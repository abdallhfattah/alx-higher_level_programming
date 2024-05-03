#!/usr/bin/python3
"""
fetch first state
"""
import sys

from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    reuslts = session.query(State, City).filter(
        State.id == City.state_id).all()
    for state, city in reuslts:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
