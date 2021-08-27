import praw
import datetime as dt
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import seaborn as sns

sns.set_palette("deep")
mpl.rcParams['axes.axisbelow'] = True
mpl.rcParams['grid.color'] = '0.8'
mpl.rcParams['figure.figsize'] = '8, 8'

from secret import CLIENT_ID, CLIENT_SECRET, USER_AGENT, USERNAME, PASSWORD

# https://praw.readthedocs.io/en/stable/getting_started/quick_start.html

# Create authorized reddit instance
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT,
    username=USERNAME,
    password=PASSWORD,
)

# Obtain specific submission
submission = reddit.submission(id='pciqyw')

# Loading all comments by making multiple api calls
# to replace all "load more comments" instances (may take a long time)
submission.comment_sort = "old"
submission.comments.replace_more(limit=None) 
all_comments = submission.comments.list()


# Create two Unix timestamps (number of seconds since 1 Jan 1970)
# Only comments between these two timestamps will be considered
time_start = dt.datetime(2021,8,26,13,0,0,
                              tzinfo=dt.timezone.utc).timestamp()
time_end = dt.datetime(2021,8,28,14,0,0,
                              tzinfo=dt.timezone.utc).timestamp()

comments  = [comment for comment in all_comments 
                        if comment.created_utc >= time_start
                          and comment.created_utc <= time_end]

comments_timestamps = [comment.created_utc for comment in comments]

df = pd.DataFrame({"datetime": pd.to_datetime(comments_timestamps, unit='s')})
min_bin = int(df['datetime'].min().floor('min').timestamp())
max_bin = int(df['datetime'].max().ceil('min').timestamp())

bin_range = list(range(min_bin, max_bin, 1800))
x_ticks = list(range(min_bin-360, max_bin+360, 3600))
minor_locator = AutoMinorLocator(6)

fig, ax = plt.subplots(figsize=(8,4))
(df["datetime"].view(int) / 10**9).hist(bins=bin_range, edgecolor='black', linewidth=1, ax=ax)
ax.set_xticks(x_ticks)
ax.xaxis.set_minor_locator(minor_locator)
ax.set_xlim(min_bin-360, max_bin+360)
labels = pd.to_datetime(ax.get_xticks().tolist(), unit='s').strftime("%X")
ax.set_xticklabels(labels, rotation=90)
plt.show()
# for comment in comments:
#   print(comment.body)
#   print('############################################')