from curses import echo
import email
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, ForeignKey, insert, select #insert and select neeed sto be imported 
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import List #get the lists
from datetime import datetime


load_dotenv()
dsn = os.getenv("DSN")

if not dsn:
    raise ValueError(
        "Missing DSN in environment variables. Create a .env file with "
        "DSN=postgresql+psycopg2://user:password@localhost:5432/dbname"
    )

engine = create_engine(dsn, echo="debug")


class Base(DeclarativeBase):
    pass


class Artist(Base):
    __tablename__ = "artist"

    constituent_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    bio: Mapped[str] = mapped_column()


class Note(Base):
    __tablename__ = 'note'

    ##name: Mapped[type] = mapped_column('constraints')

    note_id: Mapped[int] = mapped_column(primary_key=True) #an integer id, acting like a primary key
    note_text: Mapped[str] = mapped_column() #the body of the note, a ling string
    note_date: Mapped[datetime] = mapped_column() #the python default datetime is used from import, not postgres

    # OTHER TABLE 

    rental_id: Mapped[int] = mapped_column(ForeignKey('rental.rental_id')) #this is a ForeignKey, imported class


    #string and repr 
    def __str__(self):
        return f'{self.note_id}: {self.note_date} {self.note_text}'

    def __repr__(self):
        return f'{self.note_id}: {self.note_date} {self.note_text}'

class Rental(Base):
    __tablename__ = 'rental'


    rental_id : Mapped[int] = mapped_column(primary_key=True)
    scooter_num: Mapped[int] = mapped_column()
    email: Mapped[str] = mapped_column()
    start_date: Mapped[datetime] = mapped_column()
    end_date: Mapped[datetime] = mapped_column()


print(Base.metadata.tables) #TABLES POPULATED


# Basic INSERT
stmt = insert(Rental).values(
    rental_id=1,
    scooter_num=116,
    email="deniz@gmail.com",
    start_date=datetime(2024, 1, 1),
    end_date=datetime(2024, 2, 2)
)

# Basic SELECT
q = select(Rental).where(Rental.rental_id == 1)
result = session.execute(q)