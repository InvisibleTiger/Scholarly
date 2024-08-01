import streamlit as st
import requests
from streamlit_lottie import st_lottie
import json

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Streamlit page configuration
st.set_page_config(page_title="News", layout="centered", page_icon="📰")

if 'current_user' not in st.session_state or not st.session_state['current_user']:
    st.warning("Please sign in to access the news.")
else:
    st.title("News 📰")

    news = load_lottiefile("pages/assets/news.json")
    st_lottie(news, speed=1, reverse=False, loop=True, quality="low", height=None, width=None, key=None)

    def fetch_news(api_key, sources):
        base_url = "https://newsapi.org/v2/top-headlines"
        articles = []
        for source in sources:
            params = {"apiKey": api_key, "sources": source}
            response = requests.get(base_url, params=params)
            articles.extend(response.json()["articles"])
        return articles

    api_key = "7fc5e184f4604c81822c59a1a2908876"
    news_sources = ["bbc-news", "cnn", "reuters", "the-new-york-times", "the-wall-street-journal", "the-washington-post", "time", "usa-today", "vice-news", "wired"]

    articles = fetch_news(api_key, news_sources)

    for article in articles:
        st.write(f"## {article['title']}")
        st.write(f"**Source:** {article['source']['name']}")
        st.write(f"**Published At:** {article['publishedAt']}")
        st.write(f"{article['description']}")
        st.write(f"Read more: {article['url']}")

        if article['urlToImage']:
            st.image(article['urlToImage'], use_column_width=True)
        else:
            st.write("No image available.")