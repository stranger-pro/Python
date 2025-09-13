cars = [ 1, 2 , 54, "Hindi" , True]

print(cars)

print(cars[0])
print(cars[2])
print(cars[4])


print(type(cars[4]))
print(len(cars))

cars.append(3)
print(cars)
cars.append([1,2,3,4,44])
print(cars)
print(len(cars))

print(id(cars))
print(cars[-1][2])

cars = [12,32,2,3]
cars.sort() 
cars.reverse()
print(cars)