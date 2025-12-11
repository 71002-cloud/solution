"""
Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

--------

Anvend det, du har lært i dette kapitel om databaser, på en denne opgave.

Trin 1:
Opret en ny SQLite database "S2311_my_second_sql_database.db" i din solutions mappe.
Denne database skal indeholde 2 tabeller.
Den første tabel skal hedde "customers" og repræsenteres i Python-koden af en klasse kaldet "Customer".
Tabellen bruger sin første attribut "id" som primærnøgle.
De andre attributter i tabellen hedder "name", "address" og "age".
Definer selv fornuftige datatyper for attributterne.

Trin 2:
Den anden tabel skal hedde "products" og repræsenteres i Python-koden af en klasse kaldet "Product".
Denne tabel bruger også sin første attribut "id" som primærnøgle.
De andre attributter i tabellen hedder "product_number", "price" og "brand".

Trin 3:
Skriv en funktion create_test_data(), der opretter testdata for begge tabeller.

Trin 4:
Skriv en metode __repr__() for begge dataklasser, så du kan vise poster til testformål med print().

Til læsning fra databasen kan du genbruge de to funktioner select_all() og get_record() fra S2240_db_class_methods.py.

Trin 5:
Skriv hovedprogrammet: Det skriver testdata til databasen, læser dataene fra databasen med select_all() og/eller get_record() og udskriver posterne til konsollen med print().

--------

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""

from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine, select


Database = 'sqlite:///S2311_my_second_sql_database.db'
Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"Customer(id={self.id}, name={self.name}, address={self.address}, age={self.age})"

    def convert_to_tuple(self):
        return self.id, self.name, self.address, self.age

    def valid(self):
        try:
            value = int(self.age)
        except ValueError:
            return False
        return value >= 0

    @staticmethod
    def convert_from_tuple(tuple_):
        customer = Customer(id=tuple_[0], name=tuple_[1], address=tuple_[2], age=tuple_[3])
        return customer

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    product_number = Column(String)
    price = Column(Integer)
    brand = Column(String)

    def __repr__(self):
        return f"Product(id={self.id}, product_number={self.product_number}, price={self.price}, brand={self.brand})"

    def convert_to_tuple(self):
        return self.id, self.product_number, self.price, self.brand

    def valid(self):
        try:
            value = int(self.price)
        except ValueError:
            return False
        return value >= 0

    @staticmethod
    def convert_from_tuple(tuple_):
        product = Product(id=tuple_[0], product_number=tuple_[1], price=tuple_[2], brand=tuple_[3])
        return product



def select_all(classparma):
    with Session(engine) as session:
        records = session.scalars(select(classparma))
        result = []
        for record in records:
            result.append(record)
    return result

def get_record(classparma, record_id):
    with Session(engine) as session:
        records = session.scalars(select(classparma).where(classparma.id == record_id)).first()
    return records

def create_test_data():
    with Session(engine) as session:
        c1 = Customer(name="Alice", address="Main Street", age=30)
        c2 = Customer(name="Bob", address="Second Street", age=25)
        p1 = Product(product_number='100', price=199, brand="Apple")
        p2 = Product(product_number='87', price=49, brand="Sony")
        session.add_all([c1, c2, p1, p2])
        session.commit()

engine = create_engine(Database, echo=False, future=True)
Base.metadata.create_all(engine)

print(select_all(Customer))
print(select_all(Product))
print(get_record(Customer, 1))
print(get_record(Customer, 2))
print(get_record(Product, 2))