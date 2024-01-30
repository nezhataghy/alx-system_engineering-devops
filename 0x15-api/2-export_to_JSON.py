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

    with open("{}.json".format(id), "w") as file:
        json.dump({id: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        } for task in todos]}, file)


if __name__ == "__main__":
    TODO_progress(sys.argv[1])
