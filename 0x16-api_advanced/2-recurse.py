#!/usr/bin/python3
"""
Module: 2-recurse
This module contains the function `recurse` that queries the Reddit API
and returns a list of titles of all hot articles for a given subreddit.
"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and returns a list containing the titles of all
    hot articles for a given subreddit. If no results are found for the given
    subreddit, the function should return None.
    
    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of hot posts.
        after (str): The 'after' parameter for pagination.
        
    Returns:
        list: A list of titles of hot posts, or None if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after, 'limit': 100}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get('data', {})
    posts = data.get('children', [])
    after = data.get('after')

    for post in posts:
        hot_list.append(post.get('data', {}).get('title'))

    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
