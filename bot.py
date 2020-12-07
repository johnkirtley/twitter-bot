import os
import json
from time import sleep
import tweepy
import random
from datetime import datetime
# import config

# CONSUMER_KEY = config.CONSUMER_KEY
# CONSUMER_SECRET = config.CONSUMER_SECRET
# ACCESS_TOKEN = config.ACCESS_TOKEN
# ACCESS_TOKEN_SECRET = config.ACCESS_TOKEN_SECRET

def twitter_api():
    CONSUMER_KEY = os.environ["CONSUMER_KEY"]
    CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
    ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
    ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET"]

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    return api

def process():
    api = twitter_api()

    followers = api.followers_ids(api.me().id)
    friends = api.friends_ids(api.me().id)

    console.log("Unfollowing initiated")
    
    for friend in friends:
        if friend not in followers:
            api.destroy_friendship(friend)
            console.log(f"Unfollowed {friend}")

if __name__ == "__main__":
    process()



# search_terms = ["Shopify", "Ecommerce", "Shopify Store", "Dropshipping",
#                 "Shopify Seller", "Shopify Experts", "Shopify Partners"]


# class MyStreamListener(tweepy.StreamListener):
#     def __init__(self, api):
#         self.api = api
#         self.me = api.me()

#     def on_status(self, tweet):
#         me = api.me()
#         status = api.get_status(tweet.id)
#         sleep_interval = random.randint(200, 800)

#         # Likes a Tweet Within Given Parameters
#         if not status.favorited and status.favorite_count > 5:
#             api.create_favorite(tweet.id)
#             now = datetime.now()
#             current_time = now.strftime("%H:%M")

#             print(
#                 f"Time({current_time}): Liked Tweet ----- Next action in {sleep_interval // 60} minute(s)")

#             sleep(sleep_interval)

        # Follows User If Not Already Following and Within Given Parameters
        # if not tweet.user.following and tweet.user.followers_count >= 100:
        #     tweet.user.follow()
        #     now = datetime.now()
        #     current_time = now.strftime("%H:%M")

        #     print(
        #         f"Time({current_time}): Followed: {tweet.user.screen_name} ----- Next action in {sleep_interval // 60} minute(s)")

        #     sleep(sleep_interval)


        # If User Isn't Following Back and Has <= 300 Followers, Unfollow
        # friendship = api.show_friendship(me.id, tweet.user.id)
        # if tweet.user.followers_count <= 300:
        #     if friendship[0].followed_by == False:
        #         api.destroy_friendship(tweet.user.id)
        #         print(f"Unfollowing {friendship[1].screen_name}")

        #         sleep(sleep_interval)

    def on_error(self, status):
        print('Error detected')


# auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


# tweet_listener = MyStreamListener(api)
# stream = tweepy.Stream(api.auth, tweet_listener)
# stream.filter(track=search_terms, is_async=True, languages=["en"])

# with open('tweets.txt', 'r') as tweet_file:
#     tweets = tweet_file.readlines()

#     for tweet in tweets:
#         tweet_interval = random.randint(500, 800)
#         api.update_status(tweet)
#         print(f"Tweet sent")

#         sleep(tweet_interval)


# for tweet in tweepy.Cursor(api.search, q="#javascript", lang='"en').items(500):

#     status = api.get_status(tweet.id)
#     favorited = status.favorited

#     if not favorited:
#         api.create_favorite(tweet.id)
#         print("Liked Tweet")

#     if not tweet.user.following:
#         api.create_friendship(tweet.user.id)
#         print(f"Followed {tweet.user.screen_name}")

#     sleep(500)
