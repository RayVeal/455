#1. run the second demo

#2. modify the main code in client.py to add a different task 

#3. add another call to /tasks (your choice on which specific endpoint to use)

#4. submit a screenshot of the client output

import requests
import json

BASE_URL = 'http://127.0.0.1:5000'

def get_all_tasks():
    response = requests.get('http://127.0.0.1:5000/tasks')
    data = response.json()
    return data

def get_task(task_id):
    #Previous code would cause an error at line 23
    try:
        response = requests.get('http://127.0.0.1:5000/tasks/{task_id}')
        data = response.json()
        return data
    except json.decoder.JSONDecodeError:
        print('The string does NOT contain valid JSON')

def create_task(title):
    new_task = {"title": title}
    response = requests.post('http://127.0.0.1:5000/tasks', json=new_task)
    data = response.json()
    return data

#def main():
    #create_task("fish")
    
if __name__ == '__main__':
    #create_task(title="fish")
    
    all_tasks = get_all_tasks()
    print("All Tasks:")
    print(all_tasks)

    task_id = 2
    specific_task = get_task(task_id)
    print(f"\nTask {task_id}:")
    print(specific_task)

    new_task_title = "new task"
    created_task = create_task(new_task_title)
    print(f"\nCreated Task:")
    print(created_task)
    
    new_task_title = "fish"
    created_task = create_task(new_task_title)
    print(f"\nCreated Task:")
    print(created_task)
    
    #create_task(title="fish")
    #create_task(title='fish')
    #create_task("fish")
    #create_task('fish')    
    
    #main()

#create_task(title="fish")
#create_task(title='fish')
#create_task("fish")
#create_task('fish')