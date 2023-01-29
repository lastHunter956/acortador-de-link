from flask import Flask, render_template, request, redirect, url_for, flash
from pyshorteners import Shortener
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/acortar' , methods=['POST'])
def acortar():
    url = request.form['url']
    shrt = Shortener()
    nurl = shrt.tinyurl.short(url)
    print(nurl)
    return render_template('index.html', url_recortada = nurl)
if __name__ == "__main__":
    app.run( debug=True)