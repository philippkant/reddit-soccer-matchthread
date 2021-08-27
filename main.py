import praw

from secret import CLIENT_ID, CLIENT_SECRET, USER_AGENT, USERNAME, PASSWORD

reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT,
    username=USERNAME,
    password=PASSWORD,
)