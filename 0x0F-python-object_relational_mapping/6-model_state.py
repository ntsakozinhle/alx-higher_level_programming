#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def display_records():
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).all()

    for state in states:
        print(state)

    session.close()

if __name__ == "__main__":
    if len (sys.argv) != 4:
        print ("Usage: python3 6-model_state.py <username> <password> <database>")
        sys.exit(1)

    db_user, db_pass, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    db_ip = 'localhost'

    engine = create_engine(f'mysql+mysqldb://{db_user}:{db_pass}@{db_ip}/{db_name}', pool_pre_ping=True)
    Base.metadata.create_all(engine)

    display_records()
