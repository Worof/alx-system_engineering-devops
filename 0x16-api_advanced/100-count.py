#!/usr/bin/python3
import requests

def count_words(subreddit, word_list, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:subreddit.keyword.count:v1.0 (by /u/Automatic-River-2726)"}
    params = {"after": after, "limit": 100}
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        hot_list.extend([post["data"]["title"] for post in data["data"]["children"]])
        after = data["data"]["after"]
        if after is not None:
            return count_words(subreddit, word_list, hot_list, after)
        return process_words(hot_list, word_list)
    return None

def process_words(hot_list, word_list):
    word_count = {}
    word_list = [word.lower() for word in word_list]
    
    for title in hot_list:
        words = title.split()
        for word in words:
            clean_word = word.lower()
            if clean_word in word_list:
                if clean_word in word_count:
                    word_count[clean_word] += 1
                else:
                    word_count[clean_word] = 1
    
    sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    
    for word, count in sorted_word_count:
        print(f"{word}: {count}")
