import treetaggerwrapper
tagger = treetaggerwrapper.TreeTagger(TAGLANG='en',TAGDIR='/Users/Rokuden/Downloads/treetagger')
tags = tagger.TagText(u"A soccer team which has played a game was going home. Unfortunately, since the driver was exhausted, the car crushes on a black luxury car on their way. As opposed to Miura which protected the younger generation and took all the responsibility -- the conditions of the private settlement to which the Lord of a car and gangster Tanioka were sentenced ...")
for nouns in tags:
    print nouns

print tags[1]
tag_split = tags[1].split("	")
print tag_split
print tag_split[1]
