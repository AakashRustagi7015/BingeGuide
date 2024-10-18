# Binge Guide
A content-based movies and webseries recommender systems that uses cosine similarity to find similar movies and webseries on the basis of Genres, Keywords, Cast, Tagline for the user.<br>
Tech Stack used: Python, Scikit-learn, Cosine-similarity, Pandas, TfIdf Vectoriser.

# Approach
1. Combined datasets from multiple resources and perform data cleaning.
2. Split the dataset into 2 datasets one for movies and other for Netflix web series.
3. Selected these features(['Genre','Tags','cast','Rating']) of each row and vectorise those using TfIdf vectorizer.
4. Calculated the cosine similarity between each vector and return top 5 similar records found.

# Requirements Installation
Run
```bash
    pip install pandas scikit-learn
```

# How To Run
1. Clone the repository.
2. Run binge_guide.py
