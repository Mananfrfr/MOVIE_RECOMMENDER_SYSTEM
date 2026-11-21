import streamlit as st
import pickle
import pandas as pd
import os
from posters import fetch_poster


def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    recommended_movies_poster=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_poster.append(fetch_poster(movie_id, os.environ.get("TMDB_API_KEY", "")))
    return recommended_movies,recommended_movies_poster




movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
st.title('MOVIE RECOMMENDER SYSTEM')

similarity = pickle.load(open('similarity.pkl','rb'))



selected_movie_name=st.selectbox(
    "List of Movie Titles:",
    movies['title'].values

)
if st.button("Recommend"):
    names,posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5= st.columns(5)

    with col1:
        st.text(names[0])
        if posters[0]:
            st.image(posters[0])
        else:
            st.caption("Poster unavailable")

    with col2:
        st.text(names[1])
        if posters[1]:
            st.image(posters[1])
        else:
            st.caption("Poster unavailable")

    with col3:
        st.text(names[2])
        if posters[2]:
            st.image(posters[2])
        else:
            st.caption("Poster unavailable")

    with col4:
        st.text(names[3])
        if posters[3]:
            st.image(posters[3])
        else:
            st.caption("Poster unavailable")

    with col5:
        st.text(names[4])
        if posters[4]:
            st.image(posters[4])
        else:
            st.caption("Poster unavailable")