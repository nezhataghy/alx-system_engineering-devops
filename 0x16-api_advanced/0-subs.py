#!/usr/bin/python3
"""Function that queries the Reddit API"""


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers
    """
    import requests

    data = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json",
                        headers={'User-Agent': 'MyApp/4.0'},
                        allow_redirects=False)

    if data.status_code == 200:
        return int(data.json()['data']['subscribers'])
    else:
        return 0
