from flask import Flask,render_template

import urllib2
import json

app = Flask(__name__)

@app.route('/')
def root():
    u = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=7jA1A6DbTxpcOWBCJRnjbZ9APt3Yip1zZVBxK2pH")

    dic = json.loads(u.read())
    url = dic['url']
    exp = dic['explanation']

    temp = urllib2.Request("https://www.randomtext.me/api/gibberish/ul-10/7-15", headers={ 'User-Agent': 'Mozilla/5.0' })
    u2 = urllib2.urlopen(temp)
    s = u2.read()
    dic = json.loads(s)
    ul = dic['text_out']
    print ul
    
    

    return render_template("index.html",link=url,desc=exp,ul=ul)

if __name__ == '__main__':
    app.debug = True
    app.run()
    
