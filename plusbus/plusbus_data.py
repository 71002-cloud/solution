from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine, select

Database = 'sqlite:///S2311_plusbus_sql_database.db'
Base = declarative_base()

class Kunder(Base):
    __tablename__ = 'kunder'
    id = Column(Integer, primary_key=True)
    efternavn = Column(String)
    kontakt = Column(String)

    def __repr__(self):
        return f"ID: {self.id} Efternavn: {self.efternavn} Kontakt: {self.kontakt}"

    def convert_to_tuple(self):
        return self.id, self.efternavn, self.kontakt

    @staticmethod
    def convert_from_tuple(tuple_):
        kunder = Kunder(id=tuple_[0], efternavn=tuple_[1], kontakt=tuple_[2])
        return kunder

class Rejser(Base):
    __tablename__ = 'rejser'
    id = Column(Integer, primary_key=True)
    rute = Column(String)
    dato = Column(String)
    pladser = Column(Integer)

    def __repr__(self):
        return f"ID: {self.id} Rute: {self.rute} Dato: {self.dato} Pladser: {self.pladser}"

    def convert_to_tuple(self):
        return self.id, self.rute, self.dato, self.pladser

    @staticmethod
    def convert_from_tuple(tuple_):
        rejser = Rejser(id=tuple_[0], rute=tuple_[1], dato=tuple_[2], pladser=tuple_[3])
        return rejser

class Bookinger(Base):
    __tablename__ = 'booker'
    id = Column(Integer, primary_key=True)
    kunde = Column(String)
    rejse = Column(String)
    pladser = Column(Integer)

    def __repr__(self):
        f"ID {self.id} Kunde: {self.kunde} Rejse: {self.rejse} Pladser: {self.pladser}"

    def convert_to_tuple(self):
        return self.id, self.kunde, self.rejse, self.pladser

    @staticmethod
    def convert_from_tuple(tuple_):
        booking = Bookinger(id=tuple_[0], kunde=tuple_[1], rejse=tuple_[2],pladser=tuple_[3])
        return booking

engine = create_engine(Database, echo=False, future=True)
Base.metadata.create_all(engine)