"""
thiS module simply does sentiment analysis using textblob library
"""

from textblob import TextBlob


def centiment_analyse(text):
    #creating the textblob object
    
    blob = TextBlob(text) 

    #for sentiment polarity
    polarity =  blob.sentiment.polarity
    
    #cotegorization
    if polarity > 0: 
        
        sentiment = "positive"


    elif polarity < 0 :
        sentiment = "negative"

    else :
        sentiment =  "neutral"

    result = {
        "sentiment":sentiment ,
   
        "polarity" :polarity
    }
   
    return  result

  

message = input("Enter the word to analyse: ")
print(centiment_analyse(message))

