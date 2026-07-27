# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 7
# =============================================================================
#
# TASK: Console-Based To-Do List Application
#
# Build a simple to-do list program that runs entirely in the console and
# allows the user to manage their tasks interactively using a menu.
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Task
#      - Prompt the user to type a task description.
#      - Add it to the list and confirm it was added.
#
#   2. View All Tasks
#      - Display all tasks currently in the list, numbered from 1.
#      - If the list is empty, print a friendly message saying so.
#
#   3. Delete a Task
#      - Show the list of tasks with their numbers.
#      - Ask the user which task number they want to remove.
#      - Remove the task and confirm the deletion.
#      - If the task number is invalid, print an error message.
#
#   4. Quit
#      - End the program with a farewell message.

def display_menu():
	print("=============================")
	print("     TO-DO LIST MENU")
	print("=============================")
	print("1. Add task")
	print("2. View tasks")
	print("3. Delete task")
	print("4. Quit")


def add_task(tasks):
	task = input("Enter task: ").strip()
	if task:
		tasks.append(task)
		print(f'Task added: "{task}"')
	else:
		print("No task entered. Nothing added.")


def view_tasks(tasks):
	if not tasks:
		print("No tasks in your list.")
		return
	print("Your Tasks:")
	for i, t in enumerate(tasks, start=1):
		print(f"{i}. {t}")


def delete_task(tasks):
	if not tasks:
		print("No tasks to delete.")
		return
	view_tasks(tasks)
	choice = input("Enter task number to delete: ").strip()
	if not choice.isdigit():
		print("Invalid input. Please enter a number.")
		return
	idx = int(choice) - 1
	if 0 <= idx < len(tasks):
		removed = tasks.pop(idx)
		print(f'Task "{removed}" has been removed.')
	else:
		print("Invalid task number.")


def main():
	tasks = []
	while True:
		display_menu()
		choice = input("Enter your choice (1-4): ").strip()
		if choice == '1':
			add_task(tasks)
		elif choice == '2':
			view_tasks(tasks)
		elif choice == '3':
			delete_task(tasks)
		elif choice == '4':
			print("Goodbye!")
			break
		else:
			print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == '__main__':
	main()


