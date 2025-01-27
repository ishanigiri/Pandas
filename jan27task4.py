# Use Filters in Queries
# Using the Book table, filter and print:
# 1. All books by a specific author (e.g., "Author Name").
# 2. Books priced below $20.
# 3. Sort the results by price in ascending order.


from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    price = Column(Float, nullable=False)

# Create engine and session
engine = create_engine('sqlite:///store.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add books to the Book table (if not already added)
book1 = Book(title="Hidden Sadness", author="Ishani", price=29.99)
book2 = Book(title="Digital Marketing", author="Kristina", price=18.99)
book3 = Book(title="Modern Age", author="Rishika", price=99.99)
book4 = Book(title="Budget Living", author="Jane Doe", price=19.99)
book5 = Book(title="Thriving on Less", author="Sadichha", price=15.99)
session.add_all([book1, book2, book3, book4, book5])
session.commit()


# Query 1: Books priced below $20
books_below_20 = session.query(Book).filter(Book.price < 20).all()
print("\nBooks priced below $20:")
for book in books_below_20:
    print(f"Title: {book.title}, Author: {book.author}, Price: {book.price}")

# Query 2: Books sorted by price in ascending order
books_sorted_by_price = session.query(Book).order_by(Book.price).all()
print("\nBooks sorted by price (ascending):")
for book in books_sorted_by_price:
    print(f"Title: {book.title}, Author: {book.author}, Price: {book.price}")
