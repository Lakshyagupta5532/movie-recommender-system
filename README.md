# 🎬 Movie Recommendation System

A content-based movie recommendation engine that suggests similar movies based on genre, plot, cast, and crew — built as my first end-to-end machine learning project.

## 🧩 The Problem

With thousands of movies available on streaming platforms, picking what to watch next can be overwhelming. Most recommendation systems either need massive amounts of user rating data (collaborative filtering) or are black-box solutions.

I wanted to understand **how a recommendation actually works under the hood** — so I built a content-based system from scratch: one that recommends movies purely based on the *content* of the movie itself (genres, cast, plot, director), without needing any user history.

## 💡 Why I Built It This Way

This was my **first ML project**, so the goal wasn't just to get a working app — it was to understand the full pipeline: how raw data becomes a working model becomes a usable app.

I chose **content-based filtering** (over collaborative filtering) because:
- It doesn't require user interaction data, which I didn't have
- It's easier to interpret and explain — I can clearly trace *why* a movie was recommended
- It's a great entry point to learn core NLP concepts like vectorization and similarity scoring

## ⚙️ How It Works

1. **Data Collection** — Used the TMDB 5000 Movies dataset (genres, keywords, cast, crew, overview)
2. **Feature Engineering** — Parsed nested JSON-like fields (genres, cast, crew) and combined them with the movie overview into a single "tags" string per movie
3. **Vectorization** — Converted each movie's tags into numerical vectors using `CountVectorizer`
4. **Similarity Calculation** — Computed pairwise **Cosine Similarity** between all movie vectors
5. **Recommendation** — For a selected movie, the app returns the top 5 most similar movies based on similarity score
6. **Web App** — Wrapped the whole pipeline in a Streamlit interface for interactive use

## ✨ Features

- 🔍 Select any movie from a dropdown of ~4,800 movies
- 🎯 Get top 5 similar movie recommendations instantly
- ⚡ Similarity matrix computed at runtime (cached) instead of storing a large precomputed file
- 🌐 Deployed as a live web app

## 🛠️ Tech Stack

- **Python**
- **Pandas, NumPy** — data cleaning and preprocessing
- **Scikit-learn** — CountVectorizer, Cosine Similarity
- **Streamlit** — web interface and deployment

## 🚀 Live Demo

🔗 [Try it here](https://movie-recommender-system-lakshya-gupta.streamlit.app/)

## 🖥️ Run Locally

```bash
git clone https://github.com/Lakshyagupta5532/movie-recommender-system.git
cd movie-recommender-system
pip install -r requirements.txt
streamlit run app.py
```

## 📊 Dataset

[TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) (Kaggle) — includes metadata and credits for ~4,800 movies.

## 🧠 What I Learned

- Cleaning and parsing semi-structured data (JSON-like strings inside CSV columns)
- Converting text into numerical vectors using NLP techniques
- How similarity-based recommendation systems work mathematically
- Managing large files in Git — avoiding pushing oversized precomputed files by recalculating values at runtime instead
- Deploying a Python ML model as an interactive web app

## 🔮 Future Improvements

- Add movie posters using the TMDB API for a richer visual experience
- Combine with collaborative filtering for hybrid recommendations
- Add user rating/feedback loop to improve recommendation quality over time
