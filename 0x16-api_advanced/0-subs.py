#!/usr/bin/python3
"""
Module: 0-subs
This module contains the function `number_of_subscribers` that queries
the Reddit API to get the number of subscribers for a given subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, return 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return 0
    
    data = response.json()
    if 'data' in data and 'subscribers' in data['data']:
        return data['data']['subscribers']
    
    return 0
