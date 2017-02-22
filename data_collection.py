#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "715444446603714560-uh4lmJI4pFCLvHfvzX0ecBuaQKzMtqB"
access_token_secret = "Yex7ePLEEL8xnnbtkUdrK7eXOEBzhhnuHSdwVJ63c3fL9"
consumer_key = "GTELze6W86xkRqGnOBeANjpH1"
consumer_secret = "UJpaQyyYtz64NjDao93VzCog91AFlo9Uz8ajoZD1QYVvBqUjXN"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['fever', 'aids', 'hiv', 'viral', 'cold', 'std', 'infection', 'ache', 'chickenpox', 'pneumonia', 'diarrhea'])
