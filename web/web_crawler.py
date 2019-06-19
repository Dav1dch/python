import requests
import flask
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from bs4 import BeautifulSoup

app = flask.Flask(__name__)
app.secret_key = 'David'
bootstrap = Bootstrap(app)


@app.route('/realtime')
def web2():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
           'Referer': 'http://top.baidu.com/?vit=1&fr=topindex'}
    res = requests.get("http://top.baidu.com/?vit=1&fr=topindex")
    soup = BeautifulSoup(res.content.decode('GB2312', 'ignore'), 'html.parser')

    hreflist = []
    namelist = []
    hit = []

    list1 = soup.find_all('div', class_='tab-box')
    list1 = list1[0].find_all('ul')
    for k in list1:
        for a in k.find_all('a', class_='list-title'):
            namelist.append(a.string)
        for a in k.find_all('a', class_='list-title'):
            hreflist.append(a['href'])
        b = k.select('span')
        for i in range(len(b)):
            if b[i].string == None:
                continue
            if int(b[i].string)>10:
                hit.append(b[i].string)
    
    return flask.render_template('index.html', hreflist=hreflist, namelist=namelist,hit=hit ,length=len(hreflist))


@app.route('/')
def web():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
           'Referer': 'http://top.baidu.com/?vit=1&fr=topindex'}
    res = requests.get("http://top.baidu.com/?vit=1&fr=topindex")
    soup = BeautifulSoup(res.content.decode('GB2312', 'ignore'), 'html.parser')

    hreflist = []
    namelist = []
    hit = []


    list1 = soup.find_all('div', class_='tab-box')
    list1 = list1[0].find_all('ul')
    for k in list1:
        for a in k.find_all('a', class_='list-title'):
            namelist.append(a.string)
        for a in k.find_all('a', class_='list-title'):
            hreflist.append(a['href'])
        b = k.select('span')
        for i in range(len(b)):
            if b[i].string == None:
                continue
            if int(b[i].string)>10:
                hit.append(b[i].string)
    
    return flask.render_template('index.html', hreflist=hreflist, namelist=namelist,hit=hit ,length=len(hreflist))


@app.route('/7-day')
def web1():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
           'Referer': 'http://top.baidu.com/?vit=1&fr=topindex'}
    res = requests.get("http://top.baidu.com/?vit=1&fr=topindex")
    soup = BeautifulSoup(res.content.decode('GB2312', 'ignore'), 'html.parser')

    hreflist = []
    namelist = []
    hit = []

    list1 = soup.find_all('div', class_='tab-box')
    list1 = list1[1].find_all('ul')
    for k in list1:
        for a in k.find_all('a', class_='list-title'):
            namelist.append(a.string)
        for a in k.find_all('a', class_='list-title'):
            hreflist.append(a['href'])
        b = k.select('span')
        for i in range(len(b)):
            if b[i].string == None:
                continue
            if int(b[i].string)>10:
                hit.append(b[i].string)
    
    return flask.render_template('index.html', hreflist=hreflist, namelist=namelist,hit=hit ,length=len(hreflist))


if __name__ == "__main__":
    app.run(debug=True)
