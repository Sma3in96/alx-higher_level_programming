#!/usr/bin/python3
""" select states"""
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
#from slqalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sys import argv


url_db = f"mysql+mysqlconnector://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"

engine = create_engine(url_db, echo=True)

metadata = MetaData()


states_table = Table('states', metadata,
                     Column('id', Integer, primary_key=True),
                     Column('name', String(256)),
                     )


metadata.reflect(bind=engine)


class States:
    pass


mapper = Table.mapper_for(states_table)
mapper(States)


Session = sessionmaker(bind=engine)
session = Session()


states = session.query(States).all()
for States in states:
    print(f"States ID: {States.id}, Name: {States.name}")


session.close()
