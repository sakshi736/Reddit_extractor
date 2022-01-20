'''code for No. of upvotes on top 10 comments
No. of comments on top 10 comments
No. of downvotes on top 10 comments'''

import praw
import json
 
reddit_read_only = praw.Reddit(client_id="5VXQY9rsg0krP6vuaff5Zg",         # your client id
                               client_secret="V7AXW5yPBsMLwsLO21SBkSZ3fxNaIA",      # your client secret
                               user_agent="Sakchi0405")        # your user agent
 
# URL of the post
url = "https://www.reddit.com/r/india/comments/s7duwv/weekly_mental_health_discussion_thread//"
 
# Creating a submission object
submission = reddit_read_only.submission(url=url)

from praw.models import MoreComments
 
post_dict1={'post_comments':[],"post_com_up":[],"post_com_down":[]} 
for comment in submission.comments:
    if type(comment) == MoreComments:
        continue
 
    post_dict1["post_comments"].append(comment.body)

    post_dict1["post_com_up"].append(comment.ups)

    post_dict1["post_com_down"].append(comment.downs)

 with open('post_dict1.json', 'w', encoding='utf-8') as f:
    json.dump(post_dict1, f, ensure_ascii=False, indent=4)
