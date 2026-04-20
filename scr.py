from curses import echo
import email
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, ForeignKey, insert
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


r1 = "1, 116, deniz@gmail.com, 01/01/2024, 02/02/2024"

insert(Rental).values(r1)
insert(Rental).values(rental_id = 2, scooter_num = 22, email = "denizacar@gmail.com", start_date= "01/01/2024")


