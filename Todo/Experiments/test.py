def introduce(name, age, city="unknown"):
    return f"Your name is {name.title()} from {city} and you are {age} years old."


print(introduce("matt", 20))

def introduce(*list_hobbies):
    return f"Your hobbies are {list_hobbies}"


print(introduce("jogging", "running"))
