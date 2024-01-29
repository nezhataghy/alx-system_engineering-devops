#!/usr/bin/python3
"""Gather data from an API"""

import requests
import sys


def TODO_progress(id):

    task_completed = 0
    task_list = ""
    url = "https://jsonplaceholder.typicode.com/"
    json_reponse = requests.get(url + "users/{}".format(id)).json()
    name_of_emp = json_reponse.get("name")
    json_todos = requests.get(url + "users/{}/todos".format(id)).json()
    total_tasks = len(json_todos)

    for task in json_todos:
        if task.get("completed") is True:
            task_completed += 1
            task_list += "\t " + task.get("title") + "\n"

    print("Employee {} is done with tasks({}/{}):".format(name_of_emp,
                                                          task_completed,
                                                          total_tasks))
    print(task_list[:-1])


if __name__ == "__main__":
    TODO_progress(sys.argv[1])
