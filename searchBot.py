import tweepy
import time

print("LOL")

CONSUMER_KEY = '9kyzFtMANFQ6swfIVCmJogkzz'
CONSUMER_SECRET = 'tM1QAK5UzF6H5gGFjuVqolmsO8RXS8uIseTs5LS0uYlOe02FJE'
ACCESS_KEY = '1318216558519484416-6GFHARkbJzEhPj8bOUZVk8YKCYRxIU'
ACCESS_SECRET = 'zID9tqZC5Ke2gl8jHlc1k3WLXMVqJeeLbYwx0CTLS19dy'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

api.mentions_timeline()

hashtag = "#1910hours"
tweetNumber = 10

tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

def searchBot():
 for tweet in tweets:
  try:
   tweet.retweet()
   print("Retweet Done!")
   time.sleep(2)
  except tweepy.TweepError as e:
   print(e.reason)
   time.sleep(2)

searchBot()	  