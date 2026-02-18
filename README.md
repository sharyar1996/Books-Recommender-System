# 📚 Books Recommender System

A live, interactive Book Recommender System built with Python, Streamlit, and deployed on Hugging Face Spaces. This app suggests books using **Popularity-based Filtering** and **Collaborative Filtering** (cosine similarity) and displays book covers with author and rating information.

---

## 🔥 Features

- **Popular Books Tab:** Shows the top 50 books based on average ratings and number of ratings.
- **Similar Books Tab:** Users can select any book to get **top 10 similar books** using collaborative filtering.
- **Interactive UI:** Book covers, titles, and authors displayed in a responsive layout.
- **Searchable book selection:** Start typing the book name to filter and select.
- **Live Deployment:** Accessible online via Hugging Face Spaces.

---

## 🧰 Technologies Used

- Python 3.10
- Streamlit
- Pandas, NumPy
- Scikit-learn (cosine similarity)
- Hugging Face Spaces for deployment

---

## 🚀 Live Demo

Try the app here: [Books Recommender System on Hugging Face Spaces](https://huggingface.co/spaces/SharyarJavaid/Books_Recommender_System)

---

## 📂 Repository Structure

Books_Recommender_System/
│

├── streamlit_app.py # Main Streamlit app

├── pivot_table.pkl # Pivot table of books x users

├── similarity.pkl # Cosine similarity matrix

├── books.pkl # Books dataframe

├── popular_books.pkl # Top 50 popular books dataframe

├── requirements.txt # Python dependencies

└── README.md # Project overview
