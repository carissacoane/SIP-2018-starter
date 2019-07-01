'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("TwitterData/tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below! 
tweettext = []
tweetString = ""
for tweet in tweetData:
    blob = TextBlob(tweet['text'])
    tweettext.append(blob)


#my_list = [1,2,3,4,5,6]
#print(sum(my_list)/len(my_list))

# Textblob sample:
tb = TextBlob("You are the best computer scientist in existence.")
#print(tb.sentiment)

#import matplotlib as plt

#someList = [0.2, -0.3, -0.4, -1, 1, 0.3, 0.6, 0.2, 0.14, -0.16, -0.18]


#plt.xlabel('Hi')
#plt.ylabel('Number of Items')
#plt.title('Histogram of Numbers')
#plt.axis([-1.1, 1.1, 0, 6])
#plt.grid(False)n
#plt.show()

tweetBlob = textBlob(tweetString)


tweettext = []
tweetstring = ""
for tweet in tweetData:
    tweetstring += tweet['text']

print(tweetstring)
blob_polarity = []
for blob in tweettext:
    blob_polarity.append(blob.polarity)

blob_sujectivity = []
for blob in tweettext:
    blob_sujectivity.append(blob.subjectivity)

word_dict = {}

for word in tweetBlob.words:
     word_dict[word_lower()] = tweetBlob.word_counts[word.lower()]

print(word_dict)