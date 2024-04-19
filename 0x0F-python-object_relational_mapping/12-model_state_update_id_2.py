#!/usr/bin/python3
"""
Changes the nam of a State object from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./12-model_state_update_id_2.py <username> <password> <database>")
        sys.exit(1)

    db_user, db_pass, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    db_ip = 'localhost'

    engine = create_engine(f'mysql+mysqldb://{db_user}:{db_pass}@{db_ip}/{db_name}')

    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_update = session.query(State).filter_by(id=2).first()

    if state_to_update:

        state_to_update.name = "New Mexico"

        session.commit()

    session.close()
