#!/usr/bin/python3
""" select states"""
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker
from sys import argv

# Construct the database URL
url_db = f"mysql+mysqlconnector://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"

# Create the SQLAlchemy engine
engine = create_engine(url_db, echo=True)

# Create a metadata object
metadata = MetaData()

# Reflect the existing 'states' table from the database
states_table = Table('states', metadata, autoload_with=engine)

# Create a class for the existing table
class State:
    pass

# Map the class to the existing table
mapper = Table.mapper_for(states_table)
mapper(State)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Query data from the 'states' table using the State class
states = session.query(State).all()
for state in states:
    print(f"State ID: {state.id}, Name: {state.name}")

# Close the session
session.close()
