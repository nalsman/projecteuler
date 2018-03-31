import math
factors = []
devider = 600851475143

def getSmalletsFactor(num):
	squareValue = math.floor(math.sqrt(num))
	for i in range(2, squareValue):
		if(num % i == 0):
			return i
	return num

flag = 1
while flag == 1:
    factor = getSmalletsFactor(devider)
    if(factor == devider):
        factors.append(factor)
        flag = 0
        break
    else:
        factors.append(factor)
        devider = devider/factor
        flag = 1

for x in factors:
    f = getSmalletsFactor(x)
    if x == f:
        print(x)
