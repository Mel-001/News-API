from flask import render_template
from newsapi import NewsApiClient
from . import main




@main.route('/')
def index():
    newsapi = NewsApiClient(api_key="8d21ef3a971c46e88b1d74d2055ca276")
    topheadlines = newsapi.get_top_headlines(sources="fox-news")

    articles = topheadlines['articles']
    # print(articles)
    
    
    desc = []
    news = []
    img = []
    url = []

    for i in range(len(articles)):
        myarticles = articles[i]

        
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])

    mylist = zip(news, desc, img, url)



    return render_template('index.html', context= mylist)


@main.route('/bbc')
def bbc():
    newsapi = NewsApiClient(api_key="8d21ef3a971c46e88b1d74d2055ca276")
    topheadlines = newsapi.get_top_headlines(sources="bbc-news")
 
    articles = topheadlines['articles']
 
    desc = []
    news = []
    img = []
    url=[]
 
    for i in range(len(articles)):
        myarticles = articles[i]
 
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
 
    mylist = zip(news, desc, img, url)
 
    return render_template('bbc.html', context=mylist)

@main.route('/cbc')
def cbc():
    newsapi = NewsApiClient(api_key="8d21ef3a971c46e88b1d74d2055ca276")
    topheadlines = newsapi.get_top_headlines(sources="cbc-news")
 
    articles = topheadlines['articles']
 
    desc = []
    news = []
    img = []
    url =[]
 
    for i in range(len(articles)):
        myarticles = articles[i]
 
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
 
    mylist = zip(news, desc, img), url
 
    return render_template('cbc.html', context=mylist)