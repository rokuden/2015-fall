#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, treetaggerwrapper, wikipedia
from flask import Flask, render_template, request, jsonify
sys.path.append('/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages')

tagger=treetaggerwrapper.TreeTagger(TAGLANG='en',TAGDIR='/Users/Rokuden/Downloads/treetagger')
app=Flask(__name__)
 
@app.route("/")
def index():
    return '<form action="/result" method="POST"><input name="text"><input type="submit" value="search"></form>'
 
@app.route("/result", methods=['POST'])
def result(): 
    search_word=request.form['text']
    html = "<!DOCTYPE html><html><head></head><body><h3>"
    html += search_word
    html += "</h3><p>"
    html += wikipedia.summary(search_word)
    html += "</p></body></html>"
    return html
 
if __name__ == "__main__":
    app.run()
