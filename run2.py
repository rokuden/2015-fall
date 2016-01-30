#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, treetaggerwrapper, wikipedia
from flask import Flask, render_template, request, jsonify, url_for
sys.path.append('/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages')

tagger=treetaggerwrapper.TreeTagger(TAGLANG='en',TAGDIR='/Users/Rokuden/Downloads/treetagger')
app=Flask(__name__)
 
@app.route("/")
def index():
    return '<form action="/wikisearch" method="POST"><input name="text"><input type="submit" value="search"></form>'

@app.route("/result")
def result():
    #tagger = treetaggerwrapper.TreeTagger(TAGLANG='en',TAGDIR='/Users/Rokuden/Downloads/treetagger')
    #tags = tagger.TagText(u"Software developers are rooted in the written form of their code, yet they often draw diagrams representing their code. Unfortunately, we still know little about how and why they create these diagrams, and so there is little research to inform the design of visual tools to support developers work. This paper presents findings from semi-structured interviews that have been validated with a structured survey. Results show that most of the diagrams had a transient nature because of the high cost of changing whiteboard sketches to electronic renderings. Diagrams that documented design decisions were often externalized in these temporary drawings and then subsequently lost. Current visualization tools and the software development practices that we observed do not solve these issues, but these results suggest several directions for future research.")
    #for tag in tags:
        #tag_split = tag.split(" ")
        #if tag_split[1] == "NN":
            #print "<u>" 
            #print """<span onMouseover="str = '"""+(tag_split[0])+"""';clickN()">
            #print (tag_split[0])
            #print "</span>"
            #print "</u>"
        #elif tag_split[1] == "NP":
            #print "<u>"
            #print """<span onMouseover="str = '"""+(tag_split[0])+"""';clickN()">"""
            #print (tag_split[0])
            #print "</span>"
            #print "</u>"
        #elif tag_split[1] == "NNS":
            #print "<u>"
            #print """<span onMouseover="str = '"""+(tag_split[0])+"""';clickN()">"""
            #print (tag_split[0])
            #print "</span>"
            #print "</u>"
        #elif tag_split[1] == "NPS":
            #print "<u>"
            #print """<span onMouseover="str = '"""+(tag_split[0])+"""';clickN()">"""
            #print (tag_split[0])
            #print "</span>"
            #print "</u>"
        #else:
            #print (tag_split[0])
        #print """</p><script type="text/javascript">alert("aa");function clickN(){alert(str);}</script></body></html>"""
    return '<!DOCTYPE html><html><head></head><body><h3>nikoniko</h3></body></html>'
 
@app.route("/wikisearch", methods=['POST'])
def search(): 
    search_word=request.form['text']
    html = "<!DOCTYPE html><html><head></head><body><h3>"
    html += search_word
    html += "</h3><p>"
    html += wikipedia.summary(search_word)
    html += "</p></body></html>"
    return html
 

#linkroute="http://127.0.0.1:5000/wikisearch/"






if __name__ == "__main__":
    app.run()
