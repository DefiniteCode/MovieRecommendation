import streamlit as st

st.set_page_config(layout="wide")
 
st.image("assets/banner_3.png", use_container_width=True)

st.title("Welcome to The Movie Database")

st.subheader("Recently Added Movies")

recent_1 , recent_2, recent_3, recent_4, recent_5 = st.columns(5)

with recent_1:
    st.image("assets/88.webp", caption="88 Days")


with recent_2:
    st.image("assets/sunburst.webp", caption="Sunburst")


with recent_3:
    st.image("assets/call_of_vulture.webp", caption="Call of the Vulture")


with recent_4:
    st.image("assets/being_friends.webp", caption="Being Friends with a Rock")


with recent_5:
    st.image("assets/bat-killer.webp", caption="Bat-killer")



###### Popular Movies
st.subheader("Most Popular Movies")

popular_1 , popular_2, popular_3, popular_4, popular_5 = st.columns(5)

with popular_1:
    st.image("assets/blue_beetle.webp", caption="Blue Beetle")


with popular_2:
    st.image("assets/barbie.webp", caption="Barbie")


with popular_3:
    st.image("assets/guardians_vol_3.webp", caption="Guardians of the Galaxy Vol. 3	")


with popular_4:
    st.image("assets/john_wick.webp", caption="John Wick: Chapter 4	")


with popular_5:
    st.image("assets/spiderman.webp", caption="Spider-Man: Across the Spider-Verse	")



###### viewers choice
st.subheader("Viewers Choice")

vote_1 , vote_2, vote_3, vote_4, vote_5 = st.columns(5)

with vote_1:
    st.image("assets/super_mario.webp", caption="The Super Mario Bros. Movie")


with vote_2:
    st.image("assets/gran_turismo.webp", caption="Gran Turismo")


with vote_3:
    st.image("assets/nun.webp", caption="The Nun II")


with vote_4:
    st.image("assets/meg_2.webp", caption="Meg 2: The Trench")


with vote_5:
    st.image("assets/Retribution.webp", caption="Retribution")