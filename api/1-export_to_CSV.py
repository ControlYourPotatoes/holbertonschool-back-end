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
employee_username = employee_data.get("username")

# Count the number of completed tasks
completed_tasks = sum(1 for task in todos_data if task['completed'])
number_of_done_tasks = str(completed_tasks)

# Calculate the total number of tasks
total_number_of_tasks = str(len(todos_data))

# Get the total number of tasks
total_todos = len(todos_data)

# Print the first line of the output
print(f'Employee {employee_name} is done with tasks'
      f'({completed_tasks}/{total_todos}):')

    
# Print the title of each completed task
for task in todos_data:
    if task['completed']:
        print('\t ' + task['title'])

# Export data to CSV format
with open(f'{employee_id}.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    for task in todos_data:
        writer.writerow([employee_id, employee_username,
                        task['completed'], task['title']])

if __name__ == '__main__':
    pass
