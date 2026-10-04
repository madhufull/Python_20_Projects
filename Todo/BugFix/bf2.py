try:
    total_value = int(input("Enter total value: "))
    value = int(input("Enter value: "))
    calc = value/total_value * 100
    print(calc)
except ZeroDivisionError:
    print("Your total value cannot be zero")
except ValueError:
    print("You need to enter a number")

