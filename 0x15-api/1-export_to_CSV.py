#!/usr/bin/python3
"""Export to-do list to CSV"""

import csv
import requests
import sys


def TODO_progress(id):
    """export to csv"""
    url = "https://jsonplaceholder.typicode.com/"
    json_reponse = requests.get(url + "users/{}".format(id)).json()
    if json_reponse == {}:
        exit()
    name_of_emp = json_reponse["username"]
    json_todos = requests.get(url + "users/{}/todos".format(id)).json()

    todos_list = []
    for task in json_todos:
        if task.get('userId') == id:
            todos_list.append(task)

    with open(f"{id}.csv", "w", newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        for task in todos_list:
            writer.writerow([f'"{id}","{name_of_emp}",'
                            f'"{task.get("completed")}",
                            "{task.get("title")}"\n'])


if __name__ == "__main__":
    TODO_progress(sys.argv[1])
