import streamlit as st
import pandas as pd
import pickle


st.set_page_config(layout="wide")


st.image("assets/banner_3.png", use_container_width=True)

st.title("TMDB Movie Recommendation System")


# import movie data here
with open("assets/movie_data.pkl","rb") as file:
  model_df, similarities = pickle.load(file)


# function for recommend button
def get_recommendations(title):
    # Ensure exact match and safe indexing
    match = model_df[model_df['title'].str.lower() == title.lower()]
    if match.empty:
        return pd.DataFrame()

    index = match.index[0]

    similarity_scores = similarities[index]
    movie_scores = list(enumerate(similarity_scores))
    sorted_scores = sorted(movie_scores, key=lambda x: x[1], reverse=True)
    top_movies = sorted_scores[0:10]
    top_indices = [i for i, score in top_movies]
    

    return model_df.iloc[top_indices] 



option = st.selectbox(
    "Select Your Movie",
    model_df["title"].values
)


st.write("Search Results For: " + option )
# get recommendation
recommendations_df = get_recommendations(option)

#create columns for the first row of recommendations
rec_1, rec_2, rec_3, rec_4, rec_5 = st.columns(5)

#create columns for the first row of recommendations
rec_6, rec_7, rec_8, rec_9, rec_10 = st.columns(5)

#st.dataframe(recomendations_df)

### first row
with rec_1:
    st.image(recommendations_df["poster_url"].iloc[0], recommendations_df["title"].iloc[0])

with rec_2:
    st.image(recommendations_df["poster_url"].iloc[1], recommendations_df["title"].iloc[1])

with rec_3:
    st.image(recommendations_df["poster_url"].iloc[2], recommendations_df["title"].iloc[2])

with rec_4:
    st.image(recommendations_df["poster_url"].iloc[3], recommendations_df["title"].iloc[3])

with rec_5:
    st.image(recommendations_df["poster_url"].iloc[4], recommendations_df["title"].iloc[4])


### second row
with rec_6:
    st.image(recommendations_df["poster_url"].iloc[5], recommendations_df["title"].iloc[5])

with rec_7:
    st.image(recommendations_df["poster_url"].iloc[6], recommendations_df["title"].iloc[6])

with rec_8:
    st.image(recommendations_df["poster_url"].iloc[7], recommendations_df["title"].iloc[7])

with rec_9:
    st.image(recommendations_df["poster_url"].iloc[8], recommendations_df["title"].iloc[8])

with rec_10:
    st.image(recommendations_df["poster_url"].iloc[9], recommendations_df["title"].iloc[9])
