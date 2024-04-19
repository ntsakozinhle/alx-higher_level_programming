#!/usr/bin/python3
""" """
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class State(Base):
    """
    a class that represents the 'states' table in the database.
    """
    __tablename__ = 'states'


    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        """
        Return a string representaton of State instance
        """
        return f"<State(id={self.id}, name='{self.name}')>"

if __name__ == "__main__":
    if len (sys.argv) != 4:
        print ("Usage: python3 model_state.py <username> <password> <database>")
        sys.exit(1)

    db_user, db_pass, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    db_ip = 'localhost'

    engine = create_engine(f'mysql+mysqldb://{db_user}:{db_pass}@(db_ip)/{db_name}', pool_pre_ping=True)
    Base.metadata.create_all(engine)
