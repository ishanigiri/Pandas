# Delete a Record
# Add a new user, "Jane Doe" with email "jane.doe@example.com", to the User table.
# Delete the record of "Jane Doe" from the database.
# Print the remaining users to verify the deletion.
# Hint: Use session.delete()

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

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

# Create engine and session
engine = create_engine('sqlite:///store.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add a new user "Jane Doe"
jane_doe = User(name="Jane Doe", email="jane.doe@example.com")
session.add(jane_doe)
session.commit()

# Add books to the Book table
book1 = Book(title="Hidden Sadness", author="Ishani", price=299.99)
book2 = Book(title="Digital Marketing", author="Kristina", price=399.99)
book3 = Book(title="Modern Age", author="Rishika", price=199.99)
session.add_all([book1, book2, book3])
session.commit()

# Verify "Jane Doe" and books were added
print("Users and Books before deletion:")
users = session.query(User).all()
for user in users:
    print(f"User - Name: {user.name}, Email: {user.email}")

books = session.query(Book).all()
for book in books:
    print(f"Book - Title: {book.title}, Author: {book.author}, Price: {book.price}")

# Delete "Jane Doe"
user_to_delete = session.query(User).filter(User.name == "Jane Doe").first()
if user_to_delete:
    session.delete(user_to_delete)
    session.commit()

# Verify "Jane Doe" was deleted
print("\nUsers and Books after deletion:")
remaining_users = session.query(User).all()
for user in remaining_users:
    print(f"User - Name: {user.name}, Email: {user.email}")

remaining_books = session.query(Book).all()
for book in remaining_books:
    print(f"Book - Title: {book.title}, Author: {book.author}, Price: {book.price}")
