import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# loading the data from the csv file to a pandas dataframe
def recommend_movie():
    path="https://raw.githubusercontent.com/AakashRustagi7015/movies/main/movies.csv"
    movies_data=pd.read_csv(path)
    movies_data.isna().sum()
    preferences = ['genres','keywords','tagline','cast']
    for feature in preferences:
        movies_data[feature] = movies_data[feature].fillna('')
    combined_features = movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']
    vectorizer = TfidfVectorizer(stop_words='english')
    feature_vectors = vectorizer.fit_transform(combined_features)
    similarity = cosine_similarity(feature_vectors)
    list_of_all_titles = movies_data['title'].tolist()
    name=input('Enter movie name:')
    find_close_match = difflib.get_close_matches(name, list_of_all_titles,n=4,cutoff=0.6)
    if(len(find_close_match)==0):
        print('Not found in our dataset.')
        return
    else:
        print("We have found these matches:")
        for i in range(0,len(find_close_match)):
            print(i+1,'.',find_close_match[i])
        n=int(input('Enter the number which u want to search:'))
        if(n  not in(1,len(find_close_match))):
            print('Invalid Input')
            return
        else:
            name=find_close_match[n-1]
            movie_index = movies_data[movies_data.title == name]['index'].values[0]
            similarity_score = list(enumerate(similarity[movie_index]))
            sorted_score= sorted(similarity_score, key = lambda x:x[1], reverse = True) 
            print('Movies suggested for you : \n')
            i = 1
            for movie in sorted_score[1:]:
                index = movie[0]
                title_from_index = movies_data[movies_data.index==index]['title'].values[0]
                if (i<11):
                    print(i, '.',title_from_index)
                    i+=1
            return
