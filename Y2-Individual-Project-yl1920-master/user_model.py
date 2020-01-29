from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
        __tablename__='user'
        user_id = Column(Integer, primary_key = True)
        name = Column(String)
        email = Column(String)
        message = Column(String)

        def __repr__(self):
        	return("<id: {}, name: {}, email: {}, message: {}>").format(
                               self.user_id,
                               self.name,
                               self.email,
                               self.message)
