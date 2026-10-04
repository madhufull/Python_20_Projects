password = input("Enter new password: ")

result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False


digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digit"] = digit

upper = False
for i in password:
    if i.isupper():
        upper = True

result["upper"] = upper

print(result)

print(all(result.values()))

if all(result.values()) == True:
    print("Strong password")
else:
    print("Weak password")
