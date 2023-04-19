from movie_recommender import recommend_movie
from series_recommender import recommend_series

if __name__=='__main__':
    content=input("Enter the type of content(Movies/Series):")
    if(content=='Movies'):
        recommend_movie()
    elif(content=='Series'):
        recommend_series()

