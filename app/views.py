from flask import render_template
from app import app
from newsapi import NewsApiClient




@app.route('/')
def index():
    newsapi = NewsApiClient(api_key="c7414509761344ce8321cc7ae296ade4")
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


@app.route('/bbc')
def bbc():
    newsapi = NewsApiClient(api_key="c7414509761344ce8321cc7ae296ade4")
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

@app.route('/cbc')
def cbc():
    newsapi = NewsApiClient(api_key="c7414509761344ce8321cc7ae296ade4")
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