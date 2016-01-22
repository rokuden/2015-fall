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
            </title>
        </head>
        <body>
            <h3>名詞に下線を引きます</h3>
            <p> """

import treetaggerwrapper
tagger = treetaggerwrapper.TreeTagger(TAGLANG='en',TAGDIR='/Users/Rokuden/Downloads/treetagger')
tags = tagger.TagText(u"Software developers are rooted in the written form of their code, yet they often draw diagrams representing their code. Unfortunately, we still know little about how and why they create these diagrams, and so there is little research to inform the design of visual tools to support developers work. This paper presents findings from semi-structured interviews that have been validated with a structured survey. Results show that most of the diagrams had a transient nature because of the high cost of changing whiteboard sketches to electronic renderings. Diagrams that documented design decisions were often externalized in these temporary drawings and then subsequently lost. Current visualization tools and the software development practices that we observed do not solve these issues, but these results suggest several directions for future research.")
for tag in tags:
    #html_body="""<html><body>tag</body></html>"""
    #print tag
    tag_split = tag.split("	")
    #print tag_split
    #print tag_split[1]
    if tag_split[1] == "NN":
        print "<u>"
        print """<span onClick="str = '"""
        print (tag_split[0])
        print """';clickN()";>"""
        print (tag_split[0])
        print "</span>"
        print "</u>"
        #print("NOUN")
    elif tag_split[1] == "NP":
        print "<u>"
        print """<span onClick="str = '"""
        print (tag_split[0])
        print """';clickN()";>"""
        print (tag_split[0])
        print "</span>"
        print "</u>"
        #print("PROPER NOUN")
    elif tag_split[1] == "NNS":
        print "<u>"
        print """<span onClick="str = '"""
        print (tag_split[0])
        print """';clickN()";>"""
        print (tag_split[0])
        print "</span>"
        print "</u>"
    elif tag_split[1] == "NPS":
        print "<u>"
        print """<span onClick="str = '"""
        print (tag_split[0])
        print """';clickN()";>"""
        print (tag_split[0])
        print "</span>"
        print "</u>"
    else:
        print (tag_split[0])
print """       </p>
                
                <script type="text/javascript">
                alert("aa");
                function clickN(){
                    alert(str);
                }
                </script>
            </body>
        </html>"""

