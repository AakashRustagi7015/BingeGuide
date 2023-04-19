import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def recommend_series():
    path="https://raw.githubusercontent.com/AakashRustagi7015/BingeGuide/main/Netflix_Series_data.csv"
    data=pd.read_csv(path)
    # data.head(2)
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
        if(n  not in(1,len(find_close_match))):
            print('Invalid Input')
            return
        else:
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
recommend_series()