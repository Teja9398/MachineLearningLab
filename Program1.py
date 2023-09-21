#1. write a program for calculating the mean,median,mode standard deviation and variance without using predefined methods from numpy.

def mean(numbers,n):
    return sum(numbers)/n

def median(numbers,n):
    import math
    if(n%2==0):
        median = (numbers[math.floor(n/2)]+numbers[math.floor(n/2)+1])/2
    else:
        median = numbers[math.floor(n/2)]
    return median

def mode(numbers):
    mode = {}
    max = 0
    for number in numbers:
        count = 0
        for i in range(len(numbers)):
            if(number == numbers[i]):
                count +=1
            if(count>max):
                max = count
        mode[number] = count
    for number in numbers:
        if mode[number] == max:
            return number   
         
def variance(numbers,mean):
    variance =0
    for number in numbers:
        import math
        variance+= math.pow((number - mean),2)
    return variance/len(numbers)
        
        
numbers = [1,2,3,4,5,6,6]
n= len(numbers)
mean = mean(sorted(numbers),n)
variance =variance(numbers,mean)
print('mean of the entered data :',mean)
print('median of the entered data:', median(sorted(numbers),n))
print('Mode of the entered data:', mode(sorted(numbers)))
print('variance of the entered data',variance)
import math
print('variance of the entered data',math.sqrt(variance))
