#!/usr/bin/python3
"""Export to CSV"""
import requests
import sys


def TODO_progress(id):

    url = "https://jsonplaceholder.typicode.com/"
    json_reponse = requests.get(url + "users/{}".format(id)).json()
    name_of_emp = json_reponse["name"]
    json_todos = requests.get(url + "users/{}/todos".format(id)).json()

    with open(f"{id}.csv", "w") as file:
        for task in json_todos:
            file.write(f'"{id}","{name_of_emp}",'
                       f'"{task.get("completed")}","{task.get("title")}"\n')


if __name__ == "__main__":
    TODO_progress(sys.argv[1])
