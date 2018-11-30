import numpy

hardtext = numpy.loadtxt(fname='god.txt', dtype=str, delimiter="`|`", unpack=True,usecols=[0])
for i in hardtext:
    print(i)
