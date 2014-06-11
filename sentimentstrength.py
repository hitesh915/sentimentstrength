import sys

sentimentData = 'wordwithStrengthtxt.txt'
twitterData = 'input.txt'

#var will take the user input 
var = raw_input("Enter something: ")

def tweet_dict(twitterData):
    ''' (file) -> list of dictionaries
This method should take your output.txt
file and create a list of dictionaries.
'''
    twitter_list_dict = []
    #storing the user given sentance to the dictionary for the classification
    twitter_list_dict.extend([var])
    #twitter_list_dict = ["it is good not bad","good movie i love it", "hate this, really hate this movie"] you can use this if you want to work with direct list with data
    return twitter_list_dict
   
    
def sentiment_dict(sentimentData):
    ''' (file) -> dictionary
This method should take your sentiment file
and create a dictionary in the form {word: value}
'''
    afinnfile = open(sentimentData)
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score = line.split("\t") # The file is tab-delimited. "\t" means "tab character"
        scores[term] = float(score) # Convert the score to an integer.

    return scores # Print every (term, score) pair in the dictionary
    
def main():
    
    
    tweets = tweet_dict(twitterData)
    sentiment = sentiment_dict(sentimentData)
    
    '''Create a method below that loops through each tweet in your
twees_list. For each individual tweet it should add up you sentiment
score, based on the sent_dict.
'''
    for index in range(len(tweets)):
        tweet_word = tweets[index].split()
        sent_score = 0
        for word in tweet_word:
            word = word.rstrip('?:!.,;"!@')
            word = word.replace("\n", "")
            
            if word in sentiment.keys():
                sent_score = sent_score + float(sentiment[word])
                    
            else:
                sent_score = sent_score
        if float(sent_score) > 0:
             print tweets[index]
             if float(sent_score) > 0.7:
                 print sent_score
                 print 'Highly Positive Sentiment'
             else:
                print sent_score
                print 'Positive Sentiment'
             
             
        if float(sent_score) < 0:
            print tweets[index]
            if float(sent_score) < -0.7:
                 print sent_score
                 print 'Highly Negative Sentiment'
            else:
                 print sent_score
                 print 'Negative Sentiment'


        if float(sent_score) == 0:
            print tweets[index]
            print 'Neutral Sentiment'
   
if __name__ == '__main__':
    main()
