import random 
import tweepy 

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
user = api.get_user('foxnews')
user = "FoxNews "
initalPart = "Hey "
symbol = "@"
message = "looks like you need to learn some more about ubi! https://www.yang2020.com/policies/"
finalMessage = initalPart + symbol  + user + message
api.update_status(finalMessage)
# for friend in user.friends():
#    print(friend.screen_name)
