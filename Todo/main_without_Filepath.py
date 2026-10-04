# todos = []  # No longer required since we are reading lines from file - todos.txt
# Without filepath argument in function get_todos()
def get_todos():
    with open('../files/todos.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


while True:
    user_action = input("Type add or show or edit or complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo.title() + "\n")

        with open('../files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        # added index to get serial number
        for index, item in enumerate(todos):
            item = item.strip('\n')
            # index + 1 is to start from 1 instead of 0
            print(f"{index + 1}-{item}")

    elif user_action.startswith("edit"):
        try:
            todos = get_todos()

            number = int(user_action[5:])
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + "\n"

            with open('../files/todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Edit command is not valid")
            # This will ignore the rest of the lines and go back to first line
            continue

    elif user_action.startswith("complete"):
        try:
            todos = get_todos()

            number = int(user_action[9:]) - 1
            todo_to_remove = todos[number].strip("\n")
            todos.pop(number)

            with open('../files/todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item in this number")

    elif user_action.startswith("exit"):
        print('Goodbye!')
        break
    else:
        print("Unknown command")
