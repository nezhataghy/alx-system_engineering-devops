#!/usr/bin/python3
"""Sending a request to reddit API"""
import requests


def top_ten(subreddit):
    """Function send a request to reddit API"""

    headers = {'User-Agent': 'MyApp/4.0'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    data = requests.get(url=url, headers=headers, allow_redirects=False)
    if data.status_code == 200:
        hot_ten = data.json().get('data').get('children')
        if not hot_ten:
            return print("None")
        else:
            for child in hot_ten:
                print(child.get('data').get("title"))
    else:
        return print("None")
