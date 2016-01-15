#!/usr/bin/python
# -*- coding: utf-8 -*-
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
            <p>A soccer team which has played a game was going home. Unfortunately, since the driver was exhausted, the car crushes on a black luxury car on their way. As opposed to Miura which protected the younger generation and took all the responsibility -- the conditions of the private settlement to which the owner of a car and gangster Tanioka were sentenced ...
            </p>
        </body>
    </html>
    """
import treetaggerwrapper
tagger = treetaggerwrapper.TreeTagger(TAGLANG='en',TAGDIR='/Users/Rokuden/Downloads/treetagger')
tags = tagger.TagText(u"A soccer team which has played a game was going home. Unfortunately, since the driver was exhausted, the car crushes on a black luxury car on their way. As opposed to Miura which protected the younger generation and took all the responsibility -- the conditions of the private settlement to which the owner of a car and gangster Tanioka were sentenced ...")
for tag in tags:
    html_body="""<html><body>tag</body></html>"""
    #print tag
    tag_split = tag.split("	")
    #print tag_split
    #print tag_split[1]
    if tag_split[1] == "NN":
        print html_body tag　(tag_split[2])
    #print("NOUN")
    elif tag_split[1] == "NP":
        print html_body tag　(tag_split[2])
    #print("PROPER NOUN")
    elif tag_split[1] == "NNS":
        print html_body tag　(tag_split[2])
    elif tag_split[1] == "NPS":
        print(tag_split[2])
    else:
        print html_body tag　(tag_split[2])
