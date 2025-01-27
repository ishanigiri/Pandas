#Update a Record
#Using the User table (from the above example), update the email of a user whose name is "John Doe" to "new.email@example.com".
#Print the updated record to verify the change.
#Hint: Use session.query().filter() and session.commit().


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

# Define the User table
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

# Add some records to the User table for testing
user1 = User(name="John Doe", email="old.email@example.com")
session.add_all([user1])
session.commit()

# Add books to the Book table
book1 = Book(title="Hidden Sadness", author="Ishani", price=299.99)
book2 = Book(title="Digital Marketing", author="Kristina", price=399.99)
book3 = Book(title="Modern Age", author="Rishika", price=199.99)
session.add_all([book1, book2, book3])
session.commit()

# Query books
print("Books in the database:")
for book in session.query(Book):
    print(book.title, book.author, book.price)

# Update the email of the user whose name is "John Doe"
user_to_update = session.query(User).filter(User.name == "John Doe").first()
if user_to_update:
    user_to_update.email = "new.email@example.com"  # Update the email field
    session.commit()  # Commit the changes to the database

# Verify the updated record
updated_user = session.query(User).filter(User.name == "John Doe").first()
if updated_user:
    print("\nUpdated User Record:")
    print(f"Name: {updated_user.name}, Email: {updated_user.email}")
else:
    print("User name 'John Doe' not found.")
