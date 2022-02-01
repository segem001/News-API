import urllib.request,json
from .sources import NewsSources
from .article import NewsArticle
import requests
# Getting api key
api_key = None

# Getting base url
base_url = None

def configure_request(app):
    """"""
    global api_key,base_url
    api_key=app.config['API_KEY']
    base_url = app.config['BASE_URL']


def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = 'https://newsapi.org/v2/sources?apiKey={}'.format(api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_data = url.read()
        get_response = json.loads(get_data)


        sources_results = None

        if get_response['sources']:
            news_results_list = get_response['sources']
            sources_results = process_results(news_results_list)


    return sources_results

def process_results(news_list):

    sources_results = []
    for item in news_list:
        id = item.get('id')
        title = item.get('title')
        name= item.get('name')
        description = item.get('description')
        url= item.get('url')

        news_object = NewsSources(id,title,name,description,url)
        sources_results.append(news_object)

    return sources_results


############################Articles


def get_articles(name):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(name,api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_data = url.read()
        get_response = json.loads(get_data)


        articles_results = None

        if get_response['articles']:
            news_results_list = get_response['articles']
            articles_results = process_articles_results(news_results_list)


    return articles_results

def process_articles_results(news_list):

    """"""
    sources_results = []
    for item in news_list:
        author = item.get('author')
        title = item.get('title')
        description = item.get('description')
        url= item.get('url')
        urlToImage= item.get('urlToImage')
        publishedAt= item.get('publishedAt')

        if urlToImage:
            news_object = NewsArticle(author,title,description,url,urlToImage,publishedAt)
            sources_results.append(news_object)

    return sources_results


def get_category(name):
    '''
    Function that gets the json response to our url request
    '''
    get_category_url = 'https://newsapi.org/v2/top-headlines?category={}&apiKey={}'.format(name,api_key)
    # with urllib.request.urlopen(get_category_url) as url:
    #     get_data = url.read()
    #     get_response = json.loads(get_data)
    get_response=requests.get(get_category_url).json()
    category_results = None

    if get_response['articles']:
        news_results_list = get_response['articles']
        category_results = process_articles_results(news_results_list)


    return category_results



