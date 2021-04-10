import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from db import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    f_name = Column(String, index=True)
    l_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True, index=True)
    password = Column(String)


class Job(Base):

    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String,index=True)
    experience = Column(String,index=True)
    description = Column(String,index=True)
    skills = Column(String, index=True)
    no_of_vacancies = Column(Integer, index=True)
    posted_on = Column(DateTime, default=datetime.datetime.utcnow)

    application = relationship("Application", back_populates="job", cascade="delete, merge, save-update")


class Application(Base):

    __tablename__ = "application"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey("jobs.id", ondelete="CASCADE"))
    applied_on = Column(DateTime, default=datetime.datetime.utcnow)
    viewed = Column(Boolean, default=False)

    job = relationship("Job", back_populates="application")
