
# todos = []  # No longer required since we are reading lines from file - todos.txt

while True:
    user_action = input("Type add or show or edit or complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':                               
            todo = input("Enter a todo: ") + "\n"

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            # added index to get serial number
            for index, item in enumerate(todos):
                item = item.strip('\n').title()
                # index + 1 is to start from 1 instead of 0
                print(f"{index + 1}-{item}")
        case 'edit':
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()
                print(todos)

            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + "\n"

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
        case 'complete':
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            number = int(input("Number of the todo to complete: "))

            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)

        case 'exit':
            print('Goodbye!')
            break
        case _:
            print("Unknown command")
