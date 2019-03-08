import feedparser
import tweepy
import time
from dateutil import parser

class RssTweetBot:
    """

    Defines an Tweet BOT with the following properties:

    Attributes:

        consumer_key: The developer's CONSUMER API KEY.
        consumer_secret: The developer's CONSUMER API SECRET KEY.
        access_token: The developer's ACCESS TOKEN.
        access_secret: The developer's ACCESS TOKEN SECRET.
        tweetInterval: Time in seconds after which the feeds will be checked 
                       and tweets will be posted.
        urllist: List of RSS Feed links to get content for tweets.

    """
    def __init__(self,consumer_key,consumer_secret,access_token,access_secret,tweetInterval,urllist):
        
        """

        Authenticates the user using the api keys and
        creates and returns an instace of the tweet bot

        """
        self.urllist = urllist
        try:
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret,)
            auth.set_access_token(access_token,access_secret)
            self.api = tweepy.API(auth)
            self.tweetInterval=tweetInterval
            self.user=self.api.me().screen_name
        except Exception as e:
            print("!! AUTH/TOKEN ERROR : CHECK API and ACCESS KEYS")
            exit()

    def tweetUpdate(self):
        '''

            Function to start the tweet bot. It checks the feeds and 
            tweets updates after the specified interval of time.

        '''
        print("\nBot Started for TWITTER USER : "+self.user +"\n")
        lastUpdate = time.time()
        while True:
            if (time.time()-lastUpdate) < self.tweetInterval :
                continue
            print("\n!! Fetching Updates !!\n")
            for url in self.urllist:
                feed = feedparser.parse(url)
                for feeds in feed['entries']:
                    dt = parser.parse(feeds["published"]).timestamp()
                    if lastUpdate < dt:
                        print("\n**New Feed Posted From "+str(feed['feed']['title'])+'\n-->'+feeds['title']+'\n')
                        msg = feeds['title']+" "+feeds['link']
                        try:
                            self.api.update_status(msg)
                        except Exception as e: 
                            print("\n!! ERROR : "+str(e)+" !!\n")
            lastUpdate = time.time()
