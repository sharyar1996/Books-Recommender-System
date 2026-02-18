import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(page_title="Book Recommender", layout="wide")

# -------------------------------------------------
# Load Data
# -------------------------------------------------
@st.cache_data
def load_data():
    with open("pivot_table.pkl", "rb") as f:
        pivot_table = pickle.load(f)

    with open("similarity.pkl", "rb") as f:
        similarity_scores = pickle.load(f)

    with open("books.pkl", "rb") as f:
        books = pickle.load(f)

    with open("popular_books.pkl", "rb") as f:
        popular_books = pickle.load(f)

    return pivot_table, similarity_scores, books, popular_books


pivot_table, similarity_scores, books, popular_books = load_data()

# -------------------------------------------------
# Recommendation Function (Collaborative Filtering)
# -------------------------------------------------
def recommend(book_name):
    try:
        book_index = np.where(pivot_table.index == book_name)[0][0]
    except IndexError:
        return None

    sim_scores = list(enumerate(similarity_scores[book_index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]

    recommended_books = []

    for i in sim_scores:
        title = pivot_table.index[i[0]]
        book_info = books[books["title"] == title]

        if not book_info.empty:
            image = book_info["image_url"].values[0]
            author = book_info["author"].values[0]
        else:
            image = None
            author = "Unknown"

        recommended_books.append((title, author, image))

    return recommended_books


# -------------------------------------------------
# UI
# -------------------------------------------------
st.title("📚 Book Recommender System")

tab1, tab2 = st.tabs(["🔥 Top 10 Popular Books", "📖 Similar Books"])

# -------------------------------------------------
# TAB 1 — Popular Books
# -------------------------------------------------
with tab1:
    st.subheader("Most Popular Books")

    top10 = popular_books.head(10)

    cols = st.columns(5)

    for idx, (_, row) in enumerate(top10.iterrows()):
        col = cols[idx % 5]
        with col:
            st.image(row["image_url"], width=150)
            st.caption(f"{row['title']}")
            st.caption(f"👤 {row['author']}")
            st.caption(f"⭐ {round(row['avg_rating'],2)}")


# -------------------------------------------------
# TAB 2 — Collaborative Filtering
# -------------------------------------------------
with tab2:
    st.subheader("Find Similar Books")

    book_list = pivot_table.index.tolist()
    selected_book = st.selectbox("Choose a book:", book_list)

    if st.button("Recommend"):
        results = recommend(selected_book)

        if results is None:
            st.write("Book not found.")
        else:
            cols = st.columns(5)

            for col, (title, author, image) in zip(cols, results):
                with col:
                    if image:
                        st.image(row["image_url"], width=150)
                    st.caption(title)
                    st.caption(f"👤 {author}")
