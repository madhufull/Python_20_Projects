meals = ['pasta', 'pizza', 'salad']

'''
for meal in meals:
    print(meal.capitalize())
'''

for index, meal in enumerate(meals, start=1):
    print(index, meal.capitalize())
