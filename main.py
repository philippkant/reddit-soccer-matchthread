import praw

from secret import CLIENT_ID, CLIENT_SECRET, USER_AGENT, USERNAME, PASSWORD

# https://praw.readthedocs.io/en/stable/getting_started/quick_start.html

# create authorized reddit instance
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT,
    username=USERNAME,
    password=PASSWORD,
)

# obtain all comments of a specific submission (may take a long time)
submission = reddit.submission(id='pbgy9r')
submission.comments.replace_more(limit=None)
comments = submission.comments.list()