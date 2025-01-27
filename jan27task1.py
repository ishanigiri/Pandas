# Create and Query a Table
# Create a new table Book with columns:
# id (Integer, Primary Key)
# title (String, required)
# author (String, required)
# price (Float, required)
# Add three books to the table.
# Query all books and print their details.
# Hint: Use SQLAlchemy's session.add() and session.query().


#Using SQLAlchemy for database interaction
from sqlalchemy import create_engine, Column, Integer, String,  Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base= declarative_base()

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    price = Column(Float, nullable=False)

#Create engine and session
engine= create_engine('sqlite:///store.db')
Base.metadata.create_all(engine)
Session= sessionmaker(bind=engine)
session= Session()
#Add a new book
book1= Book(title="Hidden Sadness", author="Ishani", price=299.99)
book2= Book(title="Digital Marketing", author="Kristina", price=399.99)
book3= Book(title="Modern Age", author="Rishika", price=199.99)
session.add_all([book1, book2, book3])
session.commit()

#Query products
for book in session.query(Book):
    print(book.title, book.author, book.price)