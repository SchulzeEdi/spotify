import streamlit as st
import pandas as pd
import time

st.set_page_config(
    layout="wide",
    page_title="spotify songs"
)

@st.cache_data
def load_data():
    df = pd.read_csv("01 Spotify.csv")
    time.sleep(5)
    return df

df = load_data()
df_stream = df.copy()
df_stream.set_index("Artist", inplace=True)
st.line_chart(df_stream[df_stream["Stream"] > 100000000]["Stream"])

#Guardar informacao no browser, quando é mt pesado, para n ficar carregando
st.session_state["df_spotify"] = df
df.set_index("Track", inplace=True)

artists = df["Artist"].value_counts().index
artist = st.selectbox("Artista", artists)
df_filtered = df[df["Artist"] == artist]
display = st.sidebar.checkbox('Display')
if display:
    st.bar_chart(df_filtered["Stream"])

albuns = df_filtered["Album"].value_counts().index
album = st.sidebar.selectbox("Album", albuns)

df_filtered2 = df[df["Album"] == album]

col1, col2 = st.columns([0.7, 0.3])

col1.bar_chart(df_filtered2["Stream"])
col2.line_chart(df_filtered2["Danceability"])

# st.write(artist)
st.sidebar.button("test")