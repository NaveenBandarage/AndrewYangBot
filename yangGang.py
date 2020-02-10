import random 
import tweepy 
import json 
from datetime import date
import datetime
from time import sleep


#reading line by line. 
read = open("YangKey.txt", "r")
consumerKey = read.readline().strip()
consumerSecret = read.readline().strip()
accessToken = read.readline().strip()
accessTokenSecret = read.readline().strip()


#getting authorisation
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

#sending manual tweets
# status = input("Write your Yang related tweet here: ")
# api.update_status(status=status)

#Testing tweeting at a user
userName = api.user_timeline(screen_name="andrewyang")
userTweet = userName[0]

# api.update_status('@andrewyang Humanity First', userTweet.id)

#helpful for finding who follows me back or others.
#I know this isn't productive but  its just an inital stage.
# user = api.get_user('foxnews')
# user = "FoxNews "
# initalPart = "Hey "
# symbol = "@"
# # message = "looks like you need to learn some more about ubi! https://www.yang2020.com/policies/"
# finalMessage = initalPart + symbol  + user + message
# api.update_status(finalMessage)
# for friend in user.friends():
#    print(friend.screen_name)
listOfUsers = ['', '', '', '', ]
trendingTopic = api.trends_place(1)
i = 0



#loop to iterate trending topics 
# x =0
# for x in range(0, 5):
#     print(trendingTopic[0]["trends"][x]["name"])
#     trendingTopicTweet = trendingTopic[0]["trends"][x]["name"]
#     message = trendingTopicTweet + " might be trending but don't forget about @andrewyang! #YangGang #HumanityFirst"
#     print("Tweet being sent out:", message)
#     api.update_status(message)
#     x+=1



#Number of days since andrew followed me 
today = date.today()
dateArray =["2020-2-10"]
todaysDate = datetime.datetime.strptime(str(today), "%Y-%m-%d").date()
baseDate = datetime.datetime.strptime(dateArray[0], "%Y-%m-%d").date()
differenceDates =  (baseDate - todaysDate).days
print("The difference in dates is: ", differenceDates)

# #checking if yang follows us. 
# relation = api.show_friendship(source_screen_name = 'yangburner',target_screen_name = 'andrewyang')
# yangFollowing = relation[1].following
# if yangFollowing == False:
#     print("Yang is not following me")
#     message = "Day " + str(differenceDates) +" of @andrewyang not following us! #yanggang"

#     api.update_status(message)

# # #retweeting what Andrew yang says. 
# yangTweets = api.user_timeline(screen_name = "andrewyang")

# for currentTweet in yangTweets:
#     if currentTweet.text[0:2] != "RT":
#         api.retweet(currentTweet.id_str)
# print("Finished rewtweeting")

#mainstream media tweet outs. Can and will add more later.
# mediaArray = ['fox', 'cnn', 'MSNBC', 'CBSNews', 'abc', 'washingtonpost', 'nytimes', 'skynews', 'time', 'guardian' ]
# symbol ='@'
# # Either leave a custom message meaning user input for each message or just pass a message 
# mediaMessage= input("Write your Yang related tweet here: ")
# for x in mediaArray:
#         message = symbol+x +" " + mediaMessage
#         sleep(10)
#         api.update_status(status=message)

# #AutoLike anything Andrew has tweeted. 
# yangTweets = api.user_timeline(screen_name = "andrewyang")

# for currentTweet in yangTweets:
#         api.create_favorite(currentTweet.id)
# #subject to timing out
# print("Finished liking")


# #Taken from realpython
# #Goes through all my mentions and retweets.
# tweets = api.mentions_timeline()
# for tweet in tweets:
#     tweet.favorite()
#     tweet.user.follow()
#     tweet.retweet()


#Tracking tweets and favouriting them. 
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")
        tweet.favorite
       
 

    def on_error(self, status):
        print("Error detected")


tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["Andrew Yang", "Yang Gang",], languages=["en"])

