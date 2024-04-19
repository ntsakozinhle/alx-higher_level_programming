#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./8-model_state_fetch_first.py <username> <password> <database>")
        sys.exit(1)

    db_user, db_pass, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    db_ip = 'localhost'

    engine = create_engine(f'mysql+mysqldb://{db_user}:{db_pass}@{db_ip}/{db_name}')
 
    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    session.close()
