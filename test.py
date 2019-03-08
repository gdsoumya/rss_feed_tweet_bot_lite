'''

	This is simple test script to initialize the basic RSS Feed Twitter Bot 
	and to demonstrate how it can be implemented in pre-existing projects.

'''

from rss_tweet_bot import RssTweetBot

# API KEYS and ACCES TOKENS

consumer_api_key = "YOUR CONSUMER API KEY"
consumer_api_secret = "YOUR CONSUMER API SECRET KEY"
access_token = "YOUR ACCESS TOKEN"
access_token_secret = "YOUR ACCESS TOKEN SECRET"

# TWEET INTERVAL IN SECONDS

interval = 300 # 5 mins

# FEED LIST

flist = ['rss url-1','rss url-2',]


# INITIALIZE BOT

bot = RssTweetBot(consumer_api_key,consumer_api_secret,access_token,access_token_secret,interval,flist)

# START BOT

bot.tweetUpdate()
