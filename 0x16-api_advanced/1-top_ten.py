#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Reddit-API-Query"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            if not posts:
                print("None")
            for post in posts:
                print(post['data'].get('title', "None"))
        else:
            print("None")
    except requests.RequestException:
        print("None")
