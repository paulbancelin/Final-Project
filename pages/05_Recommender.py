import streamlit as st
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬"
)


@st.cache_data(persist=True)
def load_data():
    movies = pd.read_csv("data/movies.csv").copy()
    ratings = pd.read_csv("data/ratings.csv").copy()
    return movies, ratings

movies, ratings = load_data()

def clean_title(title):
    title = re.sub("[^a-zA-Z0-9 ]", "", title)
    return title

movies["clean_title"] = movies["title"].apply(clean_title)

vectorizer = TfidfVectorizer(ngram_range=(1,2))
tfidf = vectorizer.fit_transform(movies["clean_title"])

st.header("🎥 Movie Search")
def search(title):
    title = clean_title(title)
    query_vec = vectorizer.transform([title])
    similarity = cosine_similarity(query_vec, tfidf).flatten()
    indices = np.argpartition(similarity, -5)[-5:]
    results = movies.iloc[indices].iloc[::-1]
    return results

movie_input = st.text_input("🔍 Enter Movie Title", key="movie_input")
movie_list = st.empty()

st.header("🍿 Movie Recommendation")
if movie_input:
    results = search(movie_input)
    movie_list.table(results[["title", "genres"]])

@st.cache_data(persist=True)
def find_similar_movies(movie_id, ratings):
    similar_users = ratings[(ratings["movieId"] == movie_id) & (ratings["rating"] > 4)]["userId"].unique()
    similar_user_recs = ratings[(ratings["userId"].isin(similar_users)) & (ratings["rating"] > 4)]["movieId"]
    similar_user_recs = similar_user_recs.value_counts() / len(similar_users)

    similar_user_recs = similar_user_recs[similar_user_recs > .10]
    all_users = ratings[(ratings["movieId"].isin(similar_user_recs.index)) & (ratings["rating"] > 4)]
    all_user_recs = all_users["movieId"].value_counts() / len(all_users["userId"].unique())
    rec_percentages = pd.concat([similar_user_recs, all_user_recs], axis=1)
    rec_percentages.columns = ["similar", "all"]

    rec_percentages["score"] = rec_percentages["similar"] / rec_percentages["all"]
    rec_percentages = rec_percentages.sort_values("score", ascending=False)
    return rec_percentages.head(10).merge(movies, left_index=True, right_on="movieId")[["score", "title", "genres"]]

recommendation_input = st.text_input("🔍 Enter Movie Title for Recommendations", key="recommendation_input")
recommendation_list = st.empty()


if recommendation_input:
    results = search(recommendation_input)
    if len(results) > 0:
        movie_id = results.iloc[0]["movieId"]
        recommendations = find_similar_movies(movie_id, ratings)
        recommendation_list.table(recommendations[["score", "title", "genres"]])
