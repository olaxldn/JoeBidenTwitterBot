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

hashtag = "#bidenharris2020"
tweetNumber = 100000

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
import time

hashtag = "#ridinwithbiden"
tweetNumber = 100000

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
import time

hashtag = "#joebiden"
tweetNumber = 100000

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
import time

hashtag = "#uselections"
tweetNumber = 100000

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
import time

hashtag = "#elections2020"
tweetNumber = 100000

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
import time

# File used to store last used or retrieved id
FILE_NAME = 'last_seen_id.txt'

# Retrieve last seen id from txt file mentioned above
def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


# store the last seen id for next time so that the same tweets are not accessed everytime
def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


# Reply to the tweets
def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    
    #add last seen id for running script from last endpoint
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
	
    #Add Username of any one user
    timeline_tweets = api.user_timeline(last_seen_id,screen_name='@joebiden',tweet_mode='extended')
    #tweet_mode='extended' provides complete tweets

    for timeline_tweet in reversed(timeline_tweets):
        print(str(timeline_tweet.id) + ' - ' + timeline_tweet.full_text, flush=True)
        last_seen_id = timeline_tweet.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        # Replace 'Something' with a text you want to find
        if 'Joe Biden' in timeline_tweet.full_text.lower():
            print('found Something!', flush=True)
            print('responding back...', flush=True)
            
            # Replace 'Reply Something' by what you want to reply
            api.update_status('@' + timeline_tweet.user.screen_name +
                              ' $0.99 Limited Edition Joe Biden Memes for sale in my bio #ridinwithbiden', timeline_tweet.id)

while True:
	# Run Script
    reply_to_tweets()
    time.sleep(10)

# Reply to the tweets
def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    
    #add last seen id for running script from last endpoint
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
	
    #Add Username of any one user
    timeline_tweets = api.user_timeline(last_seen_id,screen_name='@joebiden',tweet_mode='extended')
    #tweet_mode='extended' provides complete tweets

    for timeline_tweet in reversed(timeline_tweets):
        print(str(timeline_tweet.id) + ' - ' + timeline_tweet.full_text, flush=True)
        last_seen_id = timeline_tweet.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        # Replace 'Something' with a text you want to find
        if 'Kamala Harris' in timeline_tweet.full_text.lower():
            print('found Something!', flush=True)
            print('responding back...', flush=True)
            
            # Replace 'Reply Something' by what you want to reply
            api.update_status('@' + timeline_tweet.user.screen_name +
                              ' $0.99 Limited Edition Joe Biden Memes for sale in my bio #ridinwithbiden', timeline_tweet.id)

while True:
	# Run Script
    reply_to_tweets()
    time.sleep(10)