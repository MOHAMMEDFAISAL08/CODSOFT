import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample dataset
data = {
    'Movie_ID': [1, 2, 3, 4, 5],
    'Title': ['Man of Steel', 'Avengers-Infinity War', 'Batman vs Superman', 'Avengers-End Game', 'The Dark Knight'],
    'Genre': ['Action Sci-Fi', 'Action Sci-Fi Thriller', 'Action Sci-Fi', 'Action Sci-Fi', 'Action Crime']
}

# Creating a DataFrame
movies_df = pd.DataFrame(data)

# User's liked movie (for example, 'Inception')
liked_movie = 'Avengers-Infinity War'

# Content-based filtering
# Step 1: Convert the genres into a matrix of TF-IDF features
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(movies_df['Genre'])

# Step 2: Find the index of the liked movie
liked_movie_index = movies_df[movies_df['Title'] == liked_movie].index[0]

# Step 3: Compute cosine similarity of the liked movie with all others
cosine_similarities = cosine_similarity(tfidf_matrix[liked_movie_index], tfidf_matrix).flatten()

# Step 4: Get indices of movies sorted by similarity score (excluding the liked movie)
similar_movies_indices = cosine_similarities.argsort()[::-1][1:]

# Step 5: Recommend top N similar movies (e.g., top 3)
N = 3
recommended_movies = movies_df.iloc[similar_movies_indices[:N]]

# Output recommended movies
print("Movies you might like:")
for title in recommended_movies['Title']:
    print(f"- {title}")

