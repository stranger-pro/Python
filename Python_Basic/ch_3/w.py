fruit = input("Enter Fruits Name : ").lower()

fruits = ['mango','apple','bananna','pineapple','guvava','papaya','grapes']

if fruit in fruits:
    fruit = fruit.capitalize()
    print(fruit,'is a fruit')
else:
    fruit = fruit.capitalize()
    print(fruit,'is not a fruit')