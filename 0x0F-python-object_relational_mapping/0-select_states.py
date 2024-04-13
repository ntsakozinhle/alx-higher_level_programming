#!/usr/bin/python3
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)

def list_states(username, password, database):
   try:
        
        engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}',
                                pool_pre_ping=True)

        Session = sessionmaker(bind=engine)

        session = Session()

        seen_names = set()
        for state in session.query(State.id, State.name).distinct().order_by(State.id):
            if state.name not in seen_names:
                print(state)
                seen_names.add(state.name)

        session.close()

   except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
