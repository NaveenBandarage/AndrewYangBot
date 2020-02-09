import random 
import tweepy 
import json 
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
x =0
for x in range(0, 5):
    print(trendingTopic[0]["trends"][x]["name"])
    trendingTopicTweet = trendingTopic[0]["trends"][x]["name"]
    message = trendingTopicTweet + "might be trending but don't forget about @andrewyang! #YangGang, #HumanityFirst"
    print("Tweet being sent out:", message)
    api.update_status(message)
    x+=1
