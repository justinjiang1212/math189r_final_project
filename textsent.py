import csv
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

truncated = pd.read_csv("/home/ec2-user/new_truncated.csv")

nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()

def getText(index):
    #get the article text from the other spreadsheet (from the index)
    row = truncated.iloc[index,0]
    return(row)

def textsent(text):
    #get text sentiment of an article text, somehow
    return(sid.polarity_scores(text))

count = {}
n =  0
total_sentiments = {}
topic_counts = {}
current_docname = None
last_sentiment = None
topic_weights = {}

#now that text sent model has been trained, iterate through news articles
with open('/home/ec2-user/doc-topics.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    first_row = next(reader)

    for row in reader:
        docname = row[0].split(",")[0]

        if docname==current_docname:
            #still on the same doc, just different topics
            try:
                topic_weights[float(row[0].split(",")[1])] += float(row[0].split(",")[2])
            except KeyError:
                topic_weights[float(row[0].split(",")[1])] = float(row[0].split(",")[2])
        else:
            #new doc!

            #update larger dicts with sentiment and topic weights
            for topic in topic_weights.keys():
                try:
                    topic_counts[topic] = topic_counts[topic] + topic_weights[topic]
                except KeyError:
                    topic_counts[topic] = topic_weights[topic]
                
                pos_sentiment = topic_weights[topic] * last_sentiment['pos']
                neg_sentiment = topic_weights[topic] * last_sentiment['neg']
                neu_sentiment = topic_weights[topic] * last_sentiment['neu']
                compound_sentiment = topic_weights[topic] * last_sentiment['compound']

                try:
                    total_sentiments[topic]['pos'] += pos_sentiment
                    total_sentiments[topic]['neg'] += neg_sentiment
                    total_sentiments[topic]['neu'] += neu_sentiment
                    total_sentiments[topic]['compound'] += compound_sentiment

                except KeyError:
                    total_sentiments[topic] = {'pos':pos_sentiment, 'neg':neg_sentiment, 'neu':neu_sentiment, 'compound':compound_sentiment}


            #reset variables
            topic_weights = {}
            current_docname = row[0].split(",")[0]
            
            #calculate sentiment of new thing
            text_index = str(row[0].split(":")[-1])[0]
            text = getText(int(text_index))
            last_sentiment = textsent(text)
            print(str(n) + ": " + str(last_sentiment))
            n+=1

    #write total_sentiment divided by total_weight (topic_counts)
with open("/home/ec2-user/output.txt","a") as output:
    string = "Topic,Pos,Neg,Neu,Compound\n"
    print(string)
    output.write(string)
    for key in total_sentiments.keys():
        pos = total_sentiments[key]['pos']/topic_counts[key]
        neg = total_sentiments[key]['neg']/topic_counts[key]
        neu = total_sentiments[key]['neu']/topic_counts[key]
        compound = total_sentiments[key]['compound']/topic_counts[key]
        string = str(int(key)) + "," + str(pos) + "," + str(neg) + "," + str(neu) + "," + str(compound) + "\n"
        print(string)
        output.write(string)
