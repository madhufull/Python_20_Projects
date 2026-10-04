

member = input("Enter the member name: ") + "\n"
file = open(
    '/Users/madhu/Documents/Study/Python_20_Projects/Experiments/members.txt', 'r')

contents = file.readlines()

contents.append(member)

file = open(
    '/Users/madhu/Documents/Study/Python_20_Projects/Experiments/members.txt', 'w')
file.writelines(contents)
file.close()
