#!/usr/bin/python3
"""Gather data from an API"""
import csv
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]

# Make a GET request to the API
response = requests.get(
    'https://jsonplaceholder.typicode.com/users/' + employee_id)

todos = requests.get(
    'https://jsonplaceholder.typicode.com/todos?userId=' + employee_id)

if response.status_code != 200 or todos.status_code != 200:
    print("Error: Failed to fetch data from the API")
    sys.exit(1)

employee_data = response.json()
todos_data = todos.json()

# Get the employee name
employee_name = employee_data.get("name")

# Count the number of completed tasks
completed_tasks = sum(1 for task in todos_data if task['completed'])
number_of_done_tasks = str(completed_tasks)

# Calculate the total number of tasks
total_number_of_tasks = str(len(todos_data))

# Print the output
print("Employee " + employee_name + " is done with tasks(" +
      number_of_done_tasks + "/" + total_number_of_tasks + "):")

# Print the title of each completed task
for task in todos_data:
    if task['completed']:
        print('\t ' + task['title'])

# Export data to CSV
filename = employee_id + ".csv"
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(
        ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
    for task in todos_data:
        writer.writerow(
            [employee_id, employee_name, task['completed'], task['title']])


if __name__ == '__main__':
    pass
