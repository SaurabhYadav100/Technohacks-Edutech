print("\n--------------------------------------------------------------")
print("                         TO-DO LIST                          ")
print("--------------------------------------------------------------")
tasks = []
def display():
    print("\n_____To-Do List_____")
    if tasks:
        for i, task in enumerate(tasks, start=1):
            print(f"\n{i}. {task}")
    else:
        print("\nEmpty list...")

# Function to add a task to the list
def add(task):
    tasks.append(task)
    print(f"\nTask '{task.upper()}' added to the list")

# Function to remove a task from the list
def remove(i):
    if 1 <= i <= len(tasks):
        n= tasks.pop(i - 1)
        print(f"\nTask '{n.upper()}' removed from the list")
    else:
        print("Invalid task index")

# Main program loop
print("\n1. Add a task")
print("2. Display tasks")
print("3. Remove a task")
print("4. Quit")
while True:
    c = input("\nEnter your choice:")
    if c == "1":
        task = input("Enter the task: ")
        add(task)
    elif c == "2":
        display()
    elif c == "3":
        i = int(input("Enter the task index to remove:"))
        remove(i)
    elif c == "4":
        print("Thank You!")
        break
    else:
        print("Invalid choice")
