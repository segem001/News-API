import os


def config():
    NEWS_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    api_key = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    API_KEY=''
    SOURCE_URL='https://newsapi.org/v2/sources?apiKey={}'.format(api_key)'
    ARTICLES_URL=''
    BASE_URL=''
    Category_URL=''

def ProdConfig(config):
    """"""
    pass

def DevConfig(config):
    """"""
    DEBUG=True 