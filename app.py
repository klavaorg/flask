#!/usr/bin/env python

from flask import Flask
# from flask.ext.heroku import Heroku
from flask import render_template
from jinja2.exceptions import TemplateNotFound
app = Flask(__name__)
# heroku = Heroku(app)
# app.jinja_env.add_extension('jinja2htmlcompress.SelectiveHTMLCompress')

@app.route('/')
@app.route('/<page>/')
def any_page(page='index'):
    try:
        return render_template(page + '.html')
    except TemplateNotFound:
        return render_template('404.html')

@app.route('/<first>/<second>/')
def page(first, second):
    try:
        return render_template(first + '/' + second + '.html')
    except TemplateNotFound:
        return render_template('404.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)