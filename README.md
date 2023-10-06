import numpy  
from scipy import stats  
  
  
Empty_list = []  
while True:  
    y = input("Insert Data: ").lower()  
    Empty_list.append(y)  
    print(Empty_list)  
    if y =='':  
        Empty_list.pop()  
    elif y == 'mean':  
        Empty_list.pop()  
        z = numpy.mean([int(item) for item in Empty_list])  
        print("Mean is",z)  
        break  
    elif y == 'median':  
        Empty_list.pop()  
        z = numpy.median([int(item) for item in Empty_list])  
        print("Median is",z)  
        break  
    elif y == 'mode':  
        Empty_list.pop()  
        z = stats.mode([int(item) for item in Empty_list])  
        print("Mode is",z)  
        break  
    elif y == 'quit':  
        Empty_list.pop()  
        print("Thank You")  
        break  
print(Empty_list)
