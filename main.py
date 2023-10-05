import numpy
from scipy import stats


data = []
while True:
    y = input("Insert data numbers: ").lower()
    data.append(y)
    print(data)
    if y =='':
        data.pop()
    elif y == 'mean':
        data.pop()
        z = numpy.mean([int(item) for item in data])
        print("Mean is",z)
        break
    elif y == 'median':
        data.pop()
        z = numpy.median([int(item) for item in data])
        print("Median is",z)
        break
    elif y == 'mode':
        data.pop()
        z = stats.mode([int(item) for item in data])
        print("Mode is",z)
        break
    elif y == 'quit':
        data.pop()
        print("Thank You")
        break
print(data)


