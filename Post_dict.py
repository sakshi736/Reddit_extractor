

import praw
import pandas as pd
 
reddit_read_only = praw.Reddit(client_id="5VXQY9rsg0krP6vuaff5Zg",         #  client id
                               client_secret="V7AXW5yPBsMLwsLO21SBkSZ3fxNaIA",      # client secret
                               user_agent="Sakchi0405")   #user id
                               
subreddit = reddit_read_only.subreddit("india")

posts = subreddit.hot(limit=10)
# Scraping the top posts of the current month

posts_dict = {"Title": [],"Post URL": [],"Num_upvote":[],
              "Total Comments": [],"Num_downvote":[],
			"Username_of_poster": []
			 }

for post in posts:
	# Title of each post
	posts_dict["Title"].append(post.title)
 
  #number of upvotes on each post
	posts_dict["Num_upvote"].append(post.ups)
 
 # Total number of comments inside the post
	posts_dict["Total Comments"].append(post.num_comments)
 
 #number of upvotes on each post
	posts_dict["Num_downvote"].append(post.downs)
 
	# Text inside a post
	#posts_dict["Post Text"].append(post.selftext)
	
	# Unique ID of each post
	posts_dict["Username"].append(post.id)
	
	# The score of a post
	posts_dict["Score"].append(post.score)
	
  # URL of each post
	posts_dict["Post URL"].append(post.url)
  
 
import json
with open('post_dict.json', 'w', encoding='utf-8') as f:
    json.dump(posts_dict, f, ensure_ascii=False, indent=4)
