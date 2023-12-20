#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests


def fetch_data():
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users = requests.get(users_url).json()
    tasks = requests.get(todos_url).json()

    user_task_dict = {}

    for user in users:
        user_id = user['id']
        username = user['username']

        user_task_dict[user_id] = [
            {
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            }
            for task in tasks if task['userId'] == user_id
        ]

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(user_task_dict, jsonfile)

if __name__ == "__main__":
    fetch_data()
