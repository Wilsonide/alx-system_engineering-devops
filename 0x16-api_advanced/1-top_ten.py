#!/usr/bin/python
"""function that queries the Reddit API and prints the titlesof the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """function that queries the Reddit API and prints the titlesof the first 10 hot posts listed for a given subreddit"""
    url = 'https://www.redit.com/r/{}/hot.json'.format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    try:
        if response.status_code == 200:
            children = response.json().get('data').get('children')
            for i in range(10):
                print(children[i].get('data').get("title"))
        else:
            print("None")
    except Exception:
        print("None")
