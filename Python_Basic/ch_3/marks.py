Marks = []

for i in range(1,6):
    Mark = int(input(f"Enter Mark Of Subject Name {i} : "))
    Marks.append(Mark)

Marks.sort()
print(f"List Of Marks Of All Subjects : {Marks} ")