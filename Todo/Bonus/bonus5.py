waiting_list = ["sen", "ben", "john"]
waiting_list.sort()

for index, w in enumerate(waiting_list):
    row = f"{index + 1}.{w.capitalize()}"
    print(row)
