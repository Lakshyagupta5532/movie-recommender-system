# Movie Recommender System

A content-based movie recommendation system that suggests similar movies based on genres, keywords, cast, and crew, using NLP and cosine similarity.

## 🎯 Overview

This project recommends top 5 similar movies for any selected movie from a dataset of ~4800 movies. It uses text vectorization and similarity scoring to find movies with matching content (genres, plot keywords, cast, director).

## 🛠️ Tech Stack

- **Python**
- **Pandas, NumPy** — data preprocessing
- **Scikit-learn** — CountVectorizer, Cosine Similarity
- **Streamlit** — web application

## ⚙️ How It Works

1. Combined movie metadata (overview, genres, keywords, cast, director) into a single text feature per movie
2. Converted text into numerical vectors using `CountVectorizer`
3. Calculated similarity between all movies using **Cosine Similarity**
4. Built a recommendation function that returns top 5 most similar movies
5. Deployed as an interactive web app using Streamlit

## 📊 Dataset

TMDB 5000 Movie Dataset (Kaggle) — includes movie metadata and credits.

## 🚀 Run Locally

```bash
git clone https://github.com/Lakshyagupta5532/movie-recommender-system.git
cd movie-recommender-system
pip install -r requirements.txt
streamlit run app.py
```

## 🔗 Live Demo

[Soon --- once deployed]

## 📌 Future Improvements

- Add movie posters using TMDB API
- Add collaborative filtering for better recommendations
- Improve UI/UX
