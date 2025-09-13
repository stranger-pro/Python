import numpy as np

l = []
for i in range(1,6):
    l.append(int(input("Enter A Number : ")))

r = np.array(l)

print(r)
print(r.ndim)