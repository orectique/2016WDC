import praw
import time
import os

reddit = praw.Reddit(
    client_id=os.getenv('ID'),
    client_secret=os.getenv('SECRET'),
    password=os.getenv('PWORD'),
    user_agent="Pierre Gasly, by u/wackome",
    username=os.getenv('UNAME'),
    ratelimit_seconds = 3600
)

print(reddit.user.me())

subreddit = reddit.subreddit("formuladank")
for submission in subreddit.stream.submissions():
    submission.upvote()
    print('Upvoted ' + submission.title)

    submission.reply(body = 'Upvoted by Pierre Gasly')
    print('Replied')

    if 'nico' in submission.title or 'rosberg' in submission.title:
        submission.reply('Are you talking about Nico Rosberg, the 2016 WDC who beat Lewis Hamilton in the same machinery?')
    time.sleep(30)