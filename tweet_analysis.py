import pandas as pd
from textblob import TextBlob
from matplotlib import pyplot as plt


def determine_sentiment(item):
    tb = TextBlob(item)

    if tb.sentiment.polarity == 0:
        return 'neutral'
    elif tb.sentiment.polarity < 0:
        return 'negative'
    else:
        return 'positive'


oli_df = pd.read_csv('oli_tweets.csv')

oli_df['label'] = oli_df['tweet'].apply(determine_sentiment)

oli_df.groupby(['label']).size().plot(kind='bar')
plt.show()
