import streamlit as st
import pickle
import pandas as pd
import requests


# Define the custom CSS for the dark background
dark_background = """
<style>
body {
    background-color: #121212; /* Set your preferred dark background color */
    color: #ffffff; /* Set the text color to contrast with the dark background */
}
</style>
"""

# Use st.markdown to apply the custom CSS
st.markdown(dark_background, unsafe_allow_html=True)

# Rest of your Streamlit app code goes here

# Rest of your Streamlit app code goes here


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=2a4e7b3187f9b6232b5261b8c879ab45'.format(movie_id))
    data = response.json()

    return "https://image.tmdb.org/t/p/w500/"+ data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies_posters = []
    recommended_movies = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)


st.title('Movie Recommender System')
selected_movie_name= st.selectbox(
    'Search Movies',
    movies['title'].values

)
if st.button('recommend'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

