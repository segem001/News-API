from flask import render_template
from ..requests import get_sources,get_articles,get_category
from . import main

@main.route("/") 
def index():
    '''View root page function that returns the index page and its data'''
    popular_sources = get_sources()
    bbc=get_articles('bbc-news')
    title_var = 'Home - Welcome to News Application'
    return render_template('index.html',popular=popular_sources,bbc=bbc)


@main.route("/article/<name>")
def article(name):
    '''View root page function that returns the index page and its data'''
    articles = get_articles(name)
    popular_sources = get_sources()
    title_var = 'Home - Welcome to News Application'
    return render_template('articles.html',articles=articles,popular=popular_sources)

@main.route("/general")
def general():
    '''View root page function that returns the index page and its data'''
    results= get_category('general')
    popular_sources = get_sources()
    title_var = 'Home - Welcome to News Application'
    return render_template('general.html',general=results,popular=popular_sources)

@main.route("/sports")
def sports():
    '''View root page function that returns the index page and its data'''
    results= get_category('sports')
    popular_sources = get_sources()
    title_var = 'Home - Welcome to News Application'
    return render_template('sports.html',sports=results,popular=popular_sources)

@main.route("/business")
def business():
    '''View root page function that returns the index page and its data'''
    results= get_category('business')
    popular_sources = get_sources()
    title_var = 'Home - Welcome to News Application'
    return render_template('business.html',business=results,popular=popular_sources)
