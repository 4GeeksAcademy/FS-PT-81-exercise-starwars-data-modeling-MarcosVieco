import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    eye_color = Column(String(250))
    gender = Column(String(250))
    height = Column(Integer)   
    mass = Column(Integer)
    planet = Column(Integer, ForeignKey('planets.id'))
    vehicle = Column(Integer, ForeignKey('vehicles.id'))
    starship = Column(Integer, ForeignKey('starships.id'))

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    climate = Column(String(250))
    diameter = Column(Integer)
    persons = relationship('Person', backref=('planet'))

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250))
    cost_in_credits = Column(Integer)
    cargo_capacity = Column(Integer)
    persons = relationship('Person', backref=('vehicle'))
    

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250))
    cost_in_credits = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    hyperdrive_rating = Column(Integer)
    persons = relationship('Person', backref=('starship'))

class Favourites(Base):
    __tablename__ = 'favourites'
    id = Column(Integer, primary_key=True)
    base_type = Column(String(250), nullable=False)
    base_id = Column(Integer, nullable=False)
git add 

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
