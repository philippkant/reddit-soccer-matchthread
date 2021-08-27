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

# obtain specific submission
submission = reddit.submission(id='pciqyw')

# loading all comments by making multiple api calls
# to replace all "load more comments" instances (may take a long time)
submission.comment_sort = "old"
submission.comments.replace_more(limit=None) 
comments = submission.comments.list()

# for comment in comments:
#   print(comment.body)
#   print('############################################')