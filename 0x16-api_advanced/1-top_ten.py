#!/usr/bin/python3
import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "python:subreddit.top.ten:v1.0 (by /u/Automatic-River-2726)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        for post in data["data"]["children"]:
            print(post["data"]["title"])
    else:
        print(None)
