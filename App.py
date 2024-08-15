import streamlit as st
import pandas as pd
import pickle
import requests


st.title('Welcome To Ibrahim Creation ')
st.header('Creator- Mohammod Ibrahim Hossain ')
st.image('2ac566bdad689373d124ed45b5b70209.jpg',caption="Creator")
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
def recommendation(movie):
    movies_index = moives[moives['title'] == movie].index[0]
    distance = similarity[movies_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    movie_titles = [] 
    recommended_movie_posters = []
    for i in movies_list:
        movie_id = moives.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        movie_titles.append(moives.iloc[i[0]].title)
    return recommended_movie_posters, movie_titles

st.title("Movie Recommendation System")

model_path = r"/mount/src/movie_/archive/src/movie_dict1.pkl2"

with open(model_path, 'rb') as model_file:
    movies_dict = pickle.load(model_file)
moives = pd.DataFrame(movies_dict)
similarity_path = r"/mount/src/movie_/archive/src/similarity.pkl2"

with open(similarity_path, 'rb') as similarity_file:
    similarity = pickle.load(similarity_file)
selected_movie_name = st.selectbox(
    'Select a movie:',
    moives['title'].values)

if st.button('Show Recommendations'):
    recommended_movie_posters, recommended_movie_titles = recommendation(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommended_movie_titles[0])
        st.image(recommended_movie_posters[0])

    with col2:
        st.text(recommended_movie_titles[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_titles[2])
        st.image(recommended_movie_posters[2])

    with col4:
        st.text(recommended_movie_titles[3])
        st.image(recommended_movie_posters[3])

    with col5:
        st.text(recommended_movie_titles[4])
        st.image(recommended_movie_posters[4])
