#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys


def TODO_progress(id):
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": id}).json()

    with open("{}.json".format(id), "w") as jsonfile:
        json.dump({id: [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
        } for t in todos]}, jsonfile)


if __name__ == "__main__":
    TODO_progress(sys.argv[1])
