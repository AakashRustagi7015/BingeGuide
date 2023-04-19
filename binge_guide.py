import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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
        if(n not in range(1,len(find_close_match)+1)):
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


def recommend_series():
    path="https://raw.githubusercontent.com/AakashRustagi7015/BingeGuide/main/Netflix_Series_data.csv"
    data=pd.read_csv(path)

    data.isna().sum()
    data.dropna(axis=0,inplace=True)
    def prepare_data(x):
        return str.lower(str(x).replace(" ", ""))
    features=['Genre','Tags','cast','Rating']
    for new_feature in features:
        data.loc[:,new_feature] = data.loc[:,new_feature].apply(prepare_data)
    data.set_index(keys='Title',inplace=True)
    data.head(2)
    def create_features(x):
        return x['Genre'] + ' ' + x['Tags'] + ' ' +x['cast']+' '+ x['Rating']
    data.loc[:, 'features'] = data.apply(create_features, axis = 1)
    vector = TfidfVectorizer(stop_words='english')
    vector_matrix = vector.fit_transform(data['features'])
    cosine_sim2 = cosine_similarity(vector_matrix, vector_matrix)
    data.reset_index(inplace = True)
    indices = pd.Series(data.index, index=data['Title'])
    list_of_all_titles = data['Title'].tolist()
    name=input('Enter series name:')
    find_close_match = difflib.get_close_matches(name, list_of_all_titles,n=5,cutoff=0.6)
    if(len(find_close_match)==0):
        print('Not found in our dataset.')
        return
    else:
        print("We have found these matches:")
        for i in range(0,len(find_close_match)):
            print(i+1,'.',find_close_match[i])
        n=int(input('Enter the number which u want to search:'))
        if(n  not in range(1,len(find_close_match)+1)):
            print('Invalid Input')
            return
        else:
            name=find_close_match[n-1]
            indx=indices[name]
            sim_score=list(enumerate(cosine_sim2[indx]))
            sorted_sim_score = sorted(sim_score, key=lambda x: x[1], reverse=True)
            k=1
            for i in sorted_sim_score[1:11]:
                indx_2=i[0]
                title_from_index = data[data.index==indx_2]['Title'].values[0]
                rating=data[data.index==indx_2]['Rating'].values[0]
                type=data[data.index==indx_2]['type'].values[0]
                print(k,'.',title_from_index)
                k+=1
            return



if __name__=='__main__':
    content=input("Enter the type of content(Movies/Series):")
    if(content=='Movies'):
        recommend_movie()
    elif(content=='Series'):
        recommend_series()

