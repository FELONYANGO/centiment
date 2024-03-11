"""
thiS module simply does sentiment analysis using textblob library
"""

from textblob import TextBlob
from textblob.en import sentiment as pattern_sentiment
from collections import Counter

def centiment_analyse(text):
    #creating the textblob  
    top_number= 1 #(highest for the most contributing number in statement)
    
    blob = TextBlob(text) 

    #for sentiment polarity
    polarity =  blob.sentiment.polarity
    statement_polarity = blob.sentiment.polarity
 
    # individual word contribution
    word_polar = {word: statement_polarity + get_word_polarity(word) for word in blob.words}

      # Most informative word
    informative_word = Counter(word_polar).most_common(top_number)

    #cotegorization
    if polarity > 0: 
        
        sentiment = "positive"


    elif polarity < 0 :
        sentiment = "negative"

    else :
        sentiment =  "neutral"

    result = {
        "sentiment":sentiment ,
   
        "polarity" :polarity,

        "top_word": informative_word
    }
   
    return  result
"""
checking if the word sentiment array is not empy
"""
def get_word_polarity(word):
    try:
        return pattern_sentiment.assessments[0][1]
    except(IndexError,AttributeError):
        return 0

    
message = input("Enter the word to analyse: ")
print(centiment_analyse(message))

