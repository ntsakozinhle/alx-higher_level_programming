#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter "a" from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./13-model_state_delete_a.py <username> <password> <database>")
        sys.exit(1)

    db_user, db_pass, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    db_ip = 'localhost'

    engine = create_engine(f'mysql+mysqldb://{db_user}:{db_pass}@{db_ip}/{db_name}')

    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_delete= session.query(State).filter(State.name.like('%a%')).all()

    if state_to_delete:

        for state in state_to_delete:
            session.delete(state)

        session.commit()

    session.close()
