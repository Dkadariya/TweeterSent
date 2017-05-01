from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import json
from analyzer import nonPhr, queryT, queryS, scount, Savg

count = []
app = Flask(__name__)
app.config.update(SEND_FILE_MAX_AGE_DEFAULT=10)

i=0 
@app.route("/", methods=['GET', 'POST'])
def hello(): 
    return render_template('home.html', data=count)

@app.route("/search/", methods=['GET', 'POST'])
def hello1(): 
    if request.method == 'POST':
        searchText=request.form['search-text']
        print searchText
        count = queryT(searchText)
        print count


    return render_template('home.html', data=count)

@app.route("/sentiment/", methods=['GET', 'POST'])
def hello3(): 
    if request.method == 'POST':
        sfilter=request.form['sent']
        print sfilter
        count = queryS(sfilter)
        print count
    return render_template('home.html', data=count)

@app.route("/scount/", methods=['GET', 'POST'])
def hello2(): 
    if request.method == 'POST':
        count = scount()
        print count
    return render_template('home.html', data=count)

@app.route("/noun_c/", methods=['GET', 'POST'])
def hello4(): 
    if request.method == 'POST':
        count = nonPhr()
        print count
    return render_template('home.html', data=count)
@app.route("/avgs/", methods=['GET', 'POST'])
def hello5(): 
    if request.method == 'POST':
        count = Savg()
        print count
    return render_template('home.html', data=count)

if __name__ == "__main__":
    app.run()