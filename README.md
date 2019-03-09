# RSS Feed Tweet Bot Lite
The 'RSS Feed Tweet Bot Lite' is a more simpler and modular alternative to the **['RSS Feed Tweet Bot'](https://github.com/gdsoumya/rss_feed_tweet_bot)**. It is a module/class that can be easily integrated into existing projects without much of any extra setup.
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

**RSS Feed Tweet Bot Lite** requires [ **Python (> Python 3.6)**](https://www.python.org/) .

### Getting the project.

```sh
$ git clone https://github.com/gdsoumya/rss_feed_tweet_bot_lite.git
or 
Download and extract the Zip-File
```
### Installing Dependencies
The Project has a few dependencies which can be installed by running.
```sh
$ pip install -r dependencies.txt 
```
## Integrating the Bot
The project comes with a '[test.py](https://github.com/gdsoumya/rss_feed_tweet_bot_lite/blob/master/test.py)' file that demonstrates how one can integrate the bot into an existing project. To create an instance of the bot, implement the following code.

```python
from rss_tweet_bot import RssTweetBot

# initialize bot
bot = RssTweetBot(<consumer api key>,<consumer api secret>,<access token>, \
                  <access token secret>,<tweet interval>,<feed list>)
# start bot
bot.tweetUpdate()
```

## Setting up the API Keys

To get help about generating the necessary API keys refer to the offical twitter **[documentation](https://developer.twitter.com/en/docs/basics/developer-portal/overview)**

## Packages Used
- **[Tweepy](http://www.tweepy.org/)** : For accessing the twitter api.
- **[Feedparser](https://pypi.org/project/feedparser/)** : For parsing feeds from RSS links.

## Author
-   **Soumya Ghosh Dastidar**

## Contributting
Any contribution/suggestions are welcomed.
