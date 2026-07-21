import argparse
# 1. Fixed the import statement to match the lib module path
from lib.models import Task, User

users = {}

def add_task(args):
    user = users.get(args.user) or User(args.user)
    users[args.user] = user
    task = Task(args.title)
    user.add_task(task)
    # 2. Added print statement expected by test_add_task
    print(f"📌 Task '{args.title}' added to {args.user}.")

def complete_task(args):
    user = users.get(args.user)
    if user:
        for task in user.tasks:
            if task.title == args.title:
                task.complete()
                return
        print("❌ Task not found.")
    else:
        print("❌ User not found.")

parser = argparse.ArgumentParser(description="Task Manager CLI")
subparsers = parser.add_subparsers()

add_parser = subparsers.add_parser("add-task", help="Add a new task")
add_parser.add_argument("user")
add_parser.add_argument("title")
add_parser.set_defaults(func=add_task)

complete_parser = subparsers.add_parser("complete-task", help="Complete a task")
complete_parser.add_argument("user")
complete_parser.add_argument("title")
complete_parser.set_defaults(func=complete_task)

# Only parse arguments and execute if run as a script directly
if __name__ == "__main__":
    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
