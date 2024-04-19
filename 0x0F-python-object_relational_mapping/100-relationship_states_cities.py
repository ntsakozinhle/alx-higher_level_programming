#!/usr/bin/python3
"""
Creates the State "California" with the "San Frascisco" in the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-relationship_states_cities.py <username> <password> <database>")
        sys.exit(1)

    db_user, db_pass, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    db_ip = 'localhost'

    engine = create_engine(f'mysql+mysqldb://{db_user}:{db_pass}@{db_ip}/{db_name}')


    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name="California")
    session.add(california)
    session.commit()

    san_francisco = City(name="San Francisco", state_id=california.id)
    session.add(san_francisco)
    session.commit()

    session.close()
