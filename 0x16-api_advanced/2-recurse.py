#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:subreddit.recurse:v1.0 (by /u/Automatic-River-2726)"}
    params = {"after": after, "limit": 100}  # Fetch up to 100 posts per request
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        hot_list.extend([post["data"]["title"] for post in data["data"]["children"]])
        after = data["data"]["after"]
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    return None
