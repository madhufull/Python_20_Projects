user_input = "What is your name?"

names = []

while True:
    name = input(user_input)
    print(name.capitalize())
    if name == 'exit':
        break
    else:
        names.append(name)

    print(names)
