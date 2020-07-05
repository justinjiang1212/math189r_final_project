import csv
import pandas as pd
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

truncated = pd.read_csv('/Users/andyliu/Downloads/truncated.csv')

count = {}
n =  0
total_sentiments = {}
topic_counts = {}
current_docname = None
last_sentiment = None
topic_weights = {}


#now that text sent model has been trained, iterate through news articles
with open('/Users/andyliu/Downloads/doc-topics.csv', newline='') as csvfile:
<<<<<<< HEAD
=======
    count = {}
    total_sentiments = {}
    topic_counts = {}
>>>>>>> parent of 36ef54e... asdfasfffew
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    first_row = next(reader)

    for row in reader:
        docname = row[0]

        if docname==current_docname:
            #still on the same doc, just different topics
            try:
                topic_weights[int(row[1])] += int(row[2])
            except ValueError:
                topic_weights[int(row[1])] = int(row[2])
        else:
            #new doc!

            #update larger dicts with sentiment and topic weights
            for topic in topic_weights.keys():
                try:
                    topic_counts[topic] = topic_counts[topic] + topic_weights[topic]
                except KeyError:
                    topic_counts[topic] = topic_weights[topic]
                
                topic_sentiment = topic_weights[topic] * last_sentiment
                try:
                    total_sentiments[topic] +=  topic_sentiment
                except KeyError:
                    total_sentiments[topic] = topic_sentiment

        

            #reset variables
            topic_weights = {}
            current_docname = row[0]
            
            #calculate sentiment of new thing
            text_index = row[0].split(":")[-1]
            text = getText(text_index)
            last_sentiment = textsent(text)

    #write total_sentiment divided by total_weight (topic_counts)
    output = open("output.txt","a")

    for key in total_sentiments.keys():
        value = total_sentiments[key]/topic_counts[key]
<<<<<<< HEAD
        string = str(key) + "," + str(value) + "\n"
        output.write(string)
=======
        string = key + "," + value + "\n"
        output.write(string)

    output.close()

def getText(index):
    #get the article text from the other spreadsheet (from the index)
    row = " ".join(truncated.iloc[index])
    return(row)

def textsent(text):
    #get text sentiment of an article text, somehow
    return(sid.polarity_scores(text))
>>>>>>> parent of 36ef54e... asdfasfffew
