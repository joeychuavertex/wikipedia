import streamlit as st
import wikipediaapi as wp
import pandas as pd

st.title("Full Article")

languages = pd.read_csv("data/language-alpha2.csv")
language_alpha2 = languages["alpha2"].tolist()
option = st.selectbox("Select language", language_alpha2, index=37)

details = wp.Wikipedia(language=option, extract_format=wp.ExtractFormat.WIKI)
search = st.text_area("Search for a topic", "Python Programming Language")
page = details.page(search)

st.write(page.text)
