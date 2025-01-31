import requests
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import matplotlib.pyplot as plt

# FreeTestAPI Configuration
BASE_URL = "https://www.freetestapi.com/api/v1/movies"

# SQLAlchemy Setup
Base = declarative_base()

# Define the UserPreference model
class UserPreference(Base):
    __tablename__ = 'preferences'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    release_date = Column(String, nullable=False)
    rating = Column(String, nullable=False)

# Create a SQLite database and session
engine = create_engine('sqlite:///user_preferences.db')
Base.metadata.create_all(engine)  # Create tables if they don't exist
Session = sessionmaker(bind=engine)
session = Session()

# Fetch Movie Data from FreeTestAPI
def fetch_movies():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data from FreeTestAPI.")
        return []

# Get User Preferences
def get_user_preferences():
    preferences = session.query(UserPreference.genre).all()
    if not preferences:
        print("No preferences found. Please add some genres.")
        return []
    return [pref[0] for pref in preferences]

# Add User Preferences
def add_user_preference(genre):
    new_preference = UserPreference(genre=genre)
    session.add(new_preference)
    session.commit()
    print(f"Added preference for genre: {genre}")

# Recommend Movies Based on Preferences
def recommend_movies(genres, movies):
    recommendations = []
    for movie in movies:
        if 'genre' in movie:
            # Convert both the movie genres and user preferences to lowercase for case-insensitive comparison
            movie_genres = [g.lower() for g in movie['genre']]  # Convert movie genres to lowercase
            user_genres = [g.lower() for g in genres]  # Convert user preferences to lowercase
            
            # Check if any of the user's preferred genres match the movie's genres
            if any(genre in movie_genres for genre in user_genres):
                recommendations.append(movie)
    return recommendations

# Visualize Recommendations
def visualize_recommendations(recommendations):
    if not recommendations:
        print("No recommendations to visualize.")
        return
    
    df = pd.DataFrame(recommendations)
    df['year'] = pd.to_datetime(df['year'], errors='coerce').dt.year
    df = df.dropna(subset=['year'])
    
    # Plot movie release years
    plt.figure(figsize=(10, 6))
    df['year'].value_counts().sort_index().plot(kind='bar', color='skyblue')
    plt.title('Movie Recommendations by Release Year')
    plt.xlabel('Release Year')
    plt.ylabel('Number of Movies')
    plt.show()

# Main Function
def main():
    while True:
        print("\n1. Add Genre Preference")
        print("2. Get Movie Recommendations")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            genre = input("Enter your favorite genre (Action, Comedy, Drama, Horror, Romance, Sci-Fi, Thriller): ")
            add_user_preference(genre)
        elif choice == '2':
            preferences = get_user_preferences()
            if preferences:
                movies = fetch_movies()
                if movies:
                    recommendations = recommend_movies(preferences, movies)
                    if recommendations:
                        print("\nRecommended Movies:")
                        for movie in recommendations[:10]:  # Show top 10 recommendations
                            print(f"{movie['title']} ({movie['year']}) - Genre: {movie['genre']}")
                        visualize_recommendations(recommendations)
                    else:
                        print("No recommendations found for your preferences.")
                else:
                    print("Failed to fetch movies.")
            else:
                print("Please add some preferences first.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
    
    session.close()

if __name__ == "__main__":
    main()
