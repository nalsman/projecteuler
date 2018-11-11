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
sum = 0
i = 2
while i < 2000000:
    if(isPrimeNumber(i)):
        sum += i
    i += 1 
print(sum)