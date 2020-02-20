import praw
import re
import time

reddit = praw.Reddit(client_id="O1X5Wey9qc-CZQ",
                     client_secret="Ed6IX0OizzQezritoxMs5HM1b-k",
                     user_agent="<script:nlp:0.0.1 (by /u/IAmYouAll)>",
                     username="IAmYouAll",
                     password="SPUC@bek7cep")

subreddits_list = ["pics", "aww", "absoluteunits", "Delightfullychubby", "funny"]
subreddit_positon = 0
post_title = "absolute unit staredown"
post_url = "https://i.imgur.com/t4G1dCR.jpg"

def post():
    global subreddits_list
    global subreddit_positon

    subreddit = reddit.subreddits(subreddits_list[subreddit_positon])
    subreddit.submit(post_title, url=post_url)
    subreddit_positon = subreddit_positon + 1

    if (subreddit_positon >= len(subreddits_list) - 1):
        post()
    else:
        print("Done")


