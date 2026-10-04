import csv

with open("../files/test.csv", 'r') as file:
    data = list(csv.reader(file))

city = input("Enter a city: ")

for row in data[1:]:      # [1:] Exclude the header
    if row[0] == city:
        print(row[1])