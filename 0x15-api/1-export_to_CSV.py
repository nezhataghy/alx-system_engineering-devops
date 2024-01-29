#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys


def TODO_progress(id):
    user_id = id
    url = "https://jsonplaceholder.typicode.com/"
    json_reponse = requests.get(url + "users/{}".format(user_id)).json()
    username = json_reponse.get("username")
    json_todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
        ) for t in json_todos]


if __name__ == "__main__":
    TODO_progress(sys.argv[1])
