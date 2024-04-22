#!/usr/bin/python3
import requests
import sys

def fetch_todo_list(employee_id):
    """ Fetch and display the TODO list progress of an employee from a REST API. """
    # API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    
    # Fetching data from the API
    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    # Check if user exists
    if user_response.status_code != 200:
        print("User not found")
        return
    
    user_data = user_response.json()
    todos_data = todos_response.json()

    # Calculate task progress
    total_tasks = len(todos_data)
    completed_tasks = len([task for task in todos_data if task['completed']])

    # Display the output
    employee_name = user_data['name']
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for task in todos_data:
        if task['completed']:
            print(f"\t {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            fetch_todo_list(employee_id)
        except ValueError:
            print("Please provide a valid integer for the employee ID.")
