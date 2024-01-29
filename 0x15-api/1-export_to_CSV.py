#!/usr/bin/python3
"""Export to CSV"""
import requests
import sys


def TODO_progress(id):

    url = "https://jsonplaceholder.typicode.com/"
    json_reponse = requests.get(url + "users/{}".format(id)).json()
    name_of_emp = json_reponse.get("name")
    json_todos = requests.get(url + "users/{}/todos".format(id)).json()

    file_name = "{}.csv".format(id)
    with open(file_name, "a") as fd:
        for task in json_todos:
            completed = task.get("completed")
            title = task.get("title")
            data = "\"{}\",\"{}\",\"{}\",\"{}\"\n".format(id,
                                                          name_of_emp,
                                                          completed,
                                                          title
                                                          )
            fd.write(data)


if __name__ == "__main__":
    TODO_progress(sys.argv[1])
