date = input("Enter Today's date: ")
mood = input("How do you rate your mood today from 1 to 10? ")
thoughts = input("Let your thoughts flow:\n")

with open(f"/Users/madhu/Documents/Study/Python_20_Projects/Journal/{date}.txt", "w") as file:
    file.write(mood + "\n")  # If you want 2 lines gap, 2 * "\n"
    file.write(thoughts + "\n")
