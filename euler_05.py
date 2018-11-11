import math
start_num = 1
end_num = 20

def isPrimeNumber(number):
    if(number < 3):
        return True
    else:
        square = math.floor(number**0.5) + 1
        for i in range(2, square):
            if (number%i==0):
                return False
        return True

def getFirstFactor(number):
    if number > 2:
        square = math.floor(number**0.5) + 1
        for i in range(2,square):
            if(number%i == 0) & isPrimeNumber(i):
                return i
    return number

def getPrimeFactors(number):
    flag = True
    factors = list()
    if(isPrimeNumber(number)):
        factors.append(number)
    else:
        while(flag):
            x = getFirstFactor(number)
            factors.append(x)
            y = int(number/x)
            if(isPrimeNumber(y)):
                factors.append(y)
                flag = False
            else:
                number = y
    return factors

def differ(a,b):
    differ = 1
    factors1 = getPrimeFactors(a)
    factors2 = getPrimeFactors(b)
    for i in factors2:
        if i not in factors1:
            differ = differ*i
        else:
            factors1.remove(i)
    return differ
 
product = 1
for i in range(1,21):
    product = product*differ(product,i)
print(product)