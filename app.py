import streamlit as st
import pickle
import pandas as pd
import os
from posters import fetch_poster
from recommendations import recommendation_indices


def recommend(movie):
    movie_index = next(i for i, title in enumerate(movies["title"]) if title == movie)
    distances = similarity[movie_index]
    movies_list = recommendation_indices(distances, movie_index)

    recommended_movies=[]
    recommended_movies_poster=[]
    for i in movies_list:
        movie_id=movies.iloc[i].movie_id
        recommended_movies.append(movies.iloc[i].title)
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

    if not names:
        st.info("No other movies are available to recommend.")
    else:
        for column, name, poster in zip(st.columns(len(names)), names, posters):
            with column:
                st.text(name)
                if poster:
                    st.image(poster)
                else:
                    st.caption("Poster unavailable")
