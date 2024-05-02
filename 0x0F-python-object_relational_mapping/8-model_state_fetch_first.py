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
    lis = session.query(State).first()
    if len(lis) == 0:
        print("Nothing")
    else:
        print(lis[0].id , lis[0].name , sep=": ")
