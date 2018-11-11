import math
def isPrimeNumber(number):
    if(number < 3):
        return True
    else:
        square = math.floor(number**0.5) + 1
        for i in range(2, square):
            if (number%i==0):
                return False
        return True

counter = 0
i = 1
while counter < 10002:
    if(isPrimeNumber(i)):
        counter += 1
    i += 1 
print(i-1)