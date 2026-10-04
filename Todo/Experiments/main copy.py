
# todos = []  # No longer required since we are reading lines from file - todos.txt

while True:
    user_action = input("Type add or show or edit or complete or exit: ")
    user_action = user_action.strip()

    if 'add' or 'new' in user_action:
        # todo = input("Enter a todo: ") + "\n"  Dont need this anymore since we include todo with user action

        todo = user_action[4:]

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo.title() + "\n")

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        # added index to get serial number
        for index, item in enumerate(todos):
            item = item.strip('\n')
            # index + 1 is to start from 1 instead of 0
            print(f"{index + 1}-{item}")
    elif 'edit' in user_action:
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()
            print(todos)

        number = int(user_action[5:])
        number = number - 1
        new_todo = input("Enter a new todo: ")
        todos[number] = new_todo + "\n"

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)
    elif 'complete' in user_action:
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        # number = int(input("Number of the todo to complete: ")) removed due to if clause introduced instead of match case
        number = int(user_action[9:])

        todo_to_remove = todos[index].strip("\n")
        todos.pop(index)

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"Todo {todo_to_remove} was removed from the list"
        print(message)

    elif 'exit' in user_action:
        print('Goodbye!')
        break
    else:
        print("Unknown command")
