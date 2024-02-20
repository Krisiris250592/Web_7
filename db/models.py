from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime
from .db import Base

# Таблиця notes, де зберігатимуться назви завдань
class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(150), nullable=False)
    group_id = Column("group_id", ForeignKey("groups.id", ondelete="CASCADE"))
    group = relationship("Group", backref="students")


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)


class Discipline(Base):
    __tablename__ = "disciplines"
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    teacher_id = Column("teacher_id", ForeignKey("teachers.id", ondelete="CASCADE"))
    teacher = relationship("Teacher", backref="disciplines")

class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    grade = Column(Integer, nullable=False)
    date_of = Column(Date, nullable=False)
    student_id = Column("student_id", ForeignKey("students.id", ondelete="CASCADE"))
    student = relationship("Student", backref="students")
    discipline_id = Column("discipline_id", ForeignKey("disciplines.id", ondelete="CASCADE"))
    discipline = relationship("Discipline", backref="disciplines")



