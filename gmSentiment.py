import tweepy
import datetime
from textblob import TextBlob


# Authenticate twitter API
consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# List of GM names
gm_names = ['Ducks Murray', 'Chayka', 'Sweeney', 'Botterill', 'Treliving', 'Ron Francis', 'Bowman', 'Sakic', 'Kekalainen', 'Nill', 'Ken Holland', 'Chiarelli', 'Tallon', 'Rob Blake', 'Chuck Fletcher', 'Bergevin', 'Poile', 'Shero', 'Garth Snow', 'Gorton', 'Dorion', 'Hextall', 'Rutherford', 'Doug Wilson', 'Doug Armstrong', 'Yzerman', 'Lamoriello', 'Jim Benning', 'McPhee', 'Brian MacLellan', 'Cheveldayoff']

# Draft dates to present
exp_date = "2017-06-21"
curr_date = str(datetime.date.today())


# Function to label sentiment
def label(analysis, threshold=0):
    if analysis.sentiment[0] > threshold:
        return 'Positive'
    else:
        return 'Negative'


# Retreive tweets and save them to csv
for gm in gm_names:
    gm_polarities = []
    # Get the tweets about GMs since the expansion draft
    gm_tweets = api.search(q=[gm], count=100, since=exp_date, until=curr_date)
    # Save tweets in csv
    with open('%s_tweets.csv' % gm, 'w') as gm_file:
        gm_file.write('tweet, sentiment, polarity\n')
        for tweet in gm_tweets:
            analysis = TextBlob(str(tweet))
            # Get label according to sentiment
            gm_polarities.append(analysis.sentiment.polarity)
            gm_file.write('%s,%s,%s\n' % (tweet.text.encode('utf8'), analysis.sentiment.polarity, label(analysis)))
