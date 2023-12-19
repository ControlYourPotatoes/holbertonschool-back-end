#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]

# Make a GET request to the API
response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
todos = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

if response.status_code != 200 or todos.status_code != 200:
    print("Error: Failed to fetch data from the API")
    sys.exit(1)

employee_data = response.json()
todos_data = todos.json()

# Get the employee name
employee_name = employee_data.get("name")

# Count the number of completed tasks
completed_tasks = [todo for todo in todos_data if todo.get("completed")]
number_of_done_tasks = len(completed_tasks)

# Calculate the total number of tasks
total_number_of_tasks = len(todos_data)

# Print the output
print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):")
for task in completed_tasks:
    task_title = task.get("title")
    print(f"\t{task_title}")