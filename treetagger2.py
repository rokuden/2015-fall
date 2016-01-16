#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages')

print 'Content-type: text/html\n'
print """
    <!DOCTYPE html>
    <html>
        <head>
            <title>
                treetagger(noun extract)
            </title>
        </head>
        <body>
            <p>A soccer team <u>which</u> has played a game was going home. Unfortunately, since the driver was exhausted, the car crushes on a black luxury car on their way. Against to Miura which protected the younger generation and took all the responsibility -- the conditions of the private settlement to which the owner of a car and gangster Tanioka were sentenced ...
            </p>
        </body>
    </html>
    """
import treetaggerwrapper
tagger = treetaggerwrapper.TreeTagger(TAGLANG='en',TAGDIR='/Users/Rokuden/Downloads/treetagger')
tags = tagger.TagText(u"A soccer team which has played a game was going home. Unfortunately, since the driver was exhausted, the car crushes on a black luxury car on their way. Against Miura which protected the younger generation and took all the responsibility -- the conditions of the private settlement to which the owner of a car and gangster Tanioka were sentenced ...")
for tag in tags:
    tag_split = tag.split("	")
    if tag_split[1] == "NN":
        print "<html><body><p><u>"
        print (tag_split[0])
        print "</u></p></body></html>"
    elif tag_split[1] == "NP":
        print "<html><body><p><u>"
        print (tag_split[0])
        print "</u></p></body></html>"
    elif tag_split[1] == "NNS":
        print "<html><body><p><u>"
        print (tag_split[0])
        print "</u></p></body></html>"
    elif tag_split[1] == "NPS":
        print "<html><body><p>"
        print (tag_split[0])
        print "</u></p></body></html><u>"
    else:
        print "<html><body><p>"
        print (tag_split[0])
        print "</p></body></html>"


