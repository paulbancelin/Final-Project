import streamlit as st

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬"
)


st.write(
    """

## OBJECTIVE
The objective of this project is to develop a movie recommendation system that will analyze and sort the movies based on the title and a score. The ultimate goal is to generate a list of the top 10 similar movies, including their titles and genres.


## DATA

### Summary:

This Movie Recommendation System is based in a dataset from MovieLens, a movie recommendation service. It contains 25.000.095 ratings across 62.423 movies from 1874 to 2019. These data were created by 162.541 users between January 09, 1995 and November 21, 2019. This dataset was generated on November 21, 2019.

The data are contained in the files `movies.csv` and `ratings.csv`.


### Movies Data File Structure (movies.csv):


Movie information is contained in the file `movies.csv`. Each line of this file after the header row represents one movie, and has the following format:

    movieId,title,genres

Movie titles are entered manually or imported from <https://www.themoviedb.org/>, and include the year of release in parentheses. 

Genres are a pipe-separated list, and are selected from the following:

* Action
* Adventure
* Animation
* Children
* Comedy
* Crime
* Documentary
* Drama
* Fantasy
* Horror
* Musical
* Mystery
* Romance
* Sci-Fi
* Thriller
* War
* Western


### Ratings Data File Structure (ratings.csv):

All ratings are contained in the file `ratings.csv`. Each line of this file after the header row represents one rating of one movie by one user, and has the following format:


- The lines within this file are ordered first by userId, then, within user, by movieId.

- Ratings are made on a 5-star scale, with half-star increments (0.5 stars - 5.0 stars).


### Movie Ids:

Only movies with at least one rating or tag are included in the dataset. These movie ids are consistent with those used on the MovieLens web site (id `1` corresponds to the URL <https://movielens.org/movies/1>). Movie ids are consistent between `ratings.csv` and `movies.csv`(the same id refers to the same movie across these two data files).



### User Ids:

Users were selected at random. All selected users had rated at least 20 movies. No demographic information is included. Each user is represented by an id, and no other information is provided. User ids are consistent between `ratings.csv` and `tags.csv` (the same id refers to the same user across the two files).


## DATA PROCESSING

I use the method of TfidfVectorizer, Natural Language Processing, a class inside of Scikit-learn library, one of the most use libraries of machine learning, because this class is used to extract text features. Convert titles or descriptions into representative numerical features. The output will be an array representing the values for each word in the documents, and a list of words. And combining it with similarity techniques, such as cosine similarity (calculate the similarity between two sets of samples) it can generate personalized recommendations based on similar movies.

TfidfVectorizer is like a friend that helps you understand how important are some words. "Tfidf" stands for "Term Frequency-Inverse Document Frequency”; Term Frequency refers to how many times a word appears and Inverse Document Frequency refers to how many total documents contain that word in a collection of documents.

Now a TfidfVectorizer combines these two things to give you an idea of how important words are in a specific document. If a word has a high term frequency and a low inverse document frequency in the total collection, then that word is considered important.

So, in summary, a TfidfVectorizer helps identify important words by taking into account how many times they appear and how many other documents mention those words.


## FINAL RESULTS

The recommendation for each movie by similar users and all users, and sorts the movies based on the title and a score to provide the top 10 similar movies with their titles and genres.


## CONCLUSION

This movie recommendation system leveraged data analysis, natural language processing, and similarity techniques to generate movie recommendations. By sorting movies based on their titles and scores, the system aimed to offering relevant suggestions for users.
"""


    
    )

