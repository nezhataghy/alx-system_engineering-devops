#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests


def TODO_progress():
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as file:
        json.dump({
            user.get("id"): [{
                "task": rep.get("title"),
                "completed": rep.get("completed"),
                "username": user.get("username")
            } for rep in requests.get(url + "todos",
                                      params={"userId": user.get("id")}).json()]
            for user in users}, file)


if __name__ == "__main__":
    TODO_progress()
