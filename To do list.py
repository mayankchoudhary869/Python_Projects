def load_tasks(filename="todo.txt"):
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename="todo.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("📭 No tasks in your to-do list.")
    else:
        print("\n📝 Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

def main():
    tasks = load_tasks()

    while True:
        print("=== TO-DO LIST MENU ===")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_tasks(tasks)

        elif choice == '2':
            task = input("Enter a new task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("✅ Task added.\n")

        elif choice == '3':
            show_tasks(tasks)
            try:
                index = int(input("Enter task number to remove: ")) - 1
                if 0 <= index < len(tasks):
                    removed = tasks.pop(index)
                    save_tasks(tasks)
                    print(f"🗑️ Task '{removed}' removed.\n")
                else:
                    print("❌ Invalid task number.\n")
            except ValueError:
                print("❌ Please enter a valid number.\n")

        elif choice == '4':
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please select from 1 to 4.\n")

if __name__ == "__main__":
    main()
