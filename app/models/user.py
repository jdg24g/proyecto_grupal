from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(50))
    fullname = Column("fullname", String(50))
    password = Column("password", String(50))

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return f"<User(name='{self.name}', fullname='{self.fullname}', password='{self.password}')>"