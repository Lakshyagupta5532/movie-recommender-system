import streamlit as st
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load movies data
movies = pickle.load(open('movies.pkl', 'rb'))

# Calculate similarity at startup (fast, takes 1-2 seconds)
@st.cache_resource
def compute_similarity():
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(movies['tags']).toarray()
    similarity = cosine_similarity(vectors)
    return similarity

similarity = compute_similarity()

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# Web app UI
st.title('Movie Recommender System')

selected_movie = st.selectbox(
    'Apni pasand ki movie select karo:',
    movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    for movie in recommendations:
        st.write(movie)