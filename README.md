sentimentstrength
=================

Sentiment classification using unsupervised learning

This project will allow you to classify sentiments of the given sentences in english. The classification will be in five different classes.

             1)Positive 
             2)Negative 
             3)Neutral 
             4)Highly Negative 
             5)Highly Positive


This is very simple to use. 

All you need to do is download two files. 1) sentistrength.py 2)wordwithStrength.txt

             Step 1) Run your python file. [as you will execute that you will be asked to input a sentance]
             
             Step 2) Input a sentance. [Limitation: Endlish Words Only]
             
             Step 3) Enjoy the Output. [it can be positive, negative, neutral, highly positive, highly negative]

As the current project is based on unsupervised learning, it is making a use of a dictionary of positive and negative words.

You can find that dictionary in wordwithStrength.txt.

Different floating point values are assigned to those positive and negative words, and classification is done based on how many positive and negative words are there in that sentance.  

For this project we have set threshold to +0.7 and -0.7, above and below that range will be considered as highly positive and highly negative respectively. 

Example: 

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

Output would be as followed. [I'm just entering "i really love that movie", and it will give me score and classification of it]

    Enter something: i really love that movie 
    Text: i really love that movie
    Score: 0.79375
    Classificatio: Highly Positive Sentiment


Hope this project wil help you. 

Feel free to contact me if you find any problem with the code. Suggestions are highly appreciated. 
