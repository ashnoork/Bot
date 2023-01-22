import tweepy 
import time

api_key = "Kkt6Yrx3wkbj6eKpvWeBlKSsC"
api_secret = "QF2lqcJCmiMrXQvrFTtdjoDtds00vpC2J5xqRS1J63mNAblyjX"
access_token = "1605315943713873921-GORryfEuAPn20WuozajWtSlwJTc690"
access_secret = "vJXUE0O2FcnawcUk2necvTWwyPC7hDkkai27pQbehEJCt"
client_id  = "THV0OEthMjgyeGF2dFE3RXlrN2o6MTpjaQ"
client_secret = "1fcQaL2u92nzi0FM4s4Mywsr9fY7MbgkJ6AvbupRZICKUqdm_4"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAO0vkwEAAAAAsLDIg%2BlGH6LAgG5qYq4wh2FuWUA%3DXSHFAyI4ycus6GIiaDrnggCweMBOvnc7L0QVCMVG3z4K2LiW7n"

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
api = tweepy.API(auth)

#create a tweet 
# client.create_tweet(text = "Hello Twitter")

#like a tweet using tweet id taken from the url 
# client.like(1606730868038533126)

# replying to a tweet using its tweet id 
# client.create_tweet(in_reply_to_tweet_id=1606730868038533126, text = "Hello User")

# displaying new tweets from the timeline to the terminal 
# we could also get other things like .id .created_at .user .media .poll
# RUN THIS AGAIN!! RUN THIS AGAIN!!!
# for tweet in api.home_timeline():
 #   print(tweet.text)

# getting the id of a twitter account 
person = client.get_user(username = "gossipgirl_6ix").data.id

# getting the tweets of a person using the id of their account
# for tweet in client.get_users_tweets(person).data:
 #   print(tweet.text)

 # creating a twitter stream which has specific key-terms 

""" search_terms = ["waterloo" "REV" "V1" "code"]

# stream class used to create the actual stream of tweets 
class MyStream(tweepy.StreamingClient): 
    # this runs as soonn as the stream is connecting and starts 
    def on_connect(self):
        print("connected")
    # runs when the stream finds a tweet matching the criteria 
    def on_tweet(self, tweet): #tweet is the tweet that the stream detects
       

       if tweet.referenced_tweets == None:
        #none means that the tweet is orginal and does not refer to any other
       # also means that the tweet is not a reply
        print(tweet.text)

        time.sleep(0.2)

stream = MyStream(bearer_token=bearer_token)

for term in search_terms:
     stream.add_rules(tweepy.StreamRule(term))
     #stream.get_rules will get all the rules if we want to dleet one later 

stream.filter(tweet_fields = ["referenced_tweets"]) """

class MyStream(tweepy.StreamingClient): 
    def on_tweet(self, tweet):
        print(tweet.text)
        try:
            client.retweet(tweet.id)

        except Exception as error:
            print(error)
   
       
stream = MyStream(bearer_token=bearer_token)

rule = tweepy.StreamRule("(#alessyafarrugia OR #programming) (-is:retweet -is:reply)")

stream.add_rules(rule )

stream.filter()