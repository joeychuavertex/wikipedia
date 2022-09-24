import streamlit as st
import wikipediaapi as wp
import pandas as pd

st.title("Summary")


languages = pd.read_csv("data/language-alpha2.csv")
language_alpha2 = languages["alpha2"].tolist()
option = st.selectbox("Select language", language_alpha2, index=37)

language = wp.Wikipedia(option)

search = st.text_area("Search for a topic", "Python Programming Language")
page = language.page(search)

st.write("Title:", page.title)
st.write("Summary:", page.summary)
st.write("Page URL:", page.fullurl)

