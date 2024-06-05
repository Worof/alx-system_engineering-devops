#!/usr/bin/python3
"""
Module: 100-count
This module contains the function `count_words` that queries the Reddit API,
parses the titles of all hot articles, and prints a sorted count of given keywords.
"""
import requests

def count_words(subreddit, word_list, hot_list=[], after=None, word_count={}):
    """
    Queries the Reddit API, parses the titles of all hot articles, and prints a sorted
    count of given keywords (case-insensitive).

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count.
        hot_list (list): A list to store the titles of hot posts.
        after (str): The 'after' parameter for pagination.
        word_count (dict): A dictionary to store the count of each keyword.

    Returns:
        None
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
        title = post.get('data', {}).get('title', "").lower().split()
        hot_list.extend(title)

    if after is not None:
        return count_words(subreddit, word_list, hot_list, after, word_count)
    
    if not word_count:
        word_count = {word.lower(): 0 for word in word_list}
    
    for word in word_list:
        count = sum(1 for title_word in hot_list if title_word == word.lower())
        word_count[word.lower()] += count
    
    sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

    for word, count in sorted_word_count:
        if count > 0:
            print(f"{word}: {count}")

    return sorted_word_count

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
