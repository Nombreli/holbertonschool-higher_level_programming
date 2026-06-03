#!/usr/bin/python3
"""Module for fetching and processing posts from an API"""

import requests
import csv


def fetch_and_print_posts():
    """Fetches posts and prints titles"""

    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetches posts and saves them into CSV file"""

    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        formatted = []
        for post in data:
            formatted.append({
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            })

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(formatted)
