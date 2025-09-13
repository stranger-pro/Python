import numpy

# Numpy is faster

r = numpy.arange(1,11)**2
s = [j**2 for j in range(1,11)]
print(r)
print(s)
