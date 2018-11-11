import datetime
def totalDivisors(number):
    if number < 2: return number
    else:
        counter = 0
        for i in range(1,number+1):
            if number%i == 0:
                counter += 1
        return counter

def getTriangleNumber(number):
    if number < 2:
        return 1
    else:
        triangleNumber = 0
        for i in range(1, number+1):
            triangleNumber += i
        return triangleNumber

onCalculating = True
counter = 0
triangleNumber = 0
start_time = datetime.datetime.now().timestamp()
while(onCalculating):
    divisors = totalDivisors(triangleNumber)
    # print(triangleNumber, divisors)
    if(divisors >= 500):
        onCalculating = False
        print(triangleNumber)
    counter += 1
    triangleNumber += counter
end_time = datetime.datetime.now().timestamp()
gap_time = (end_time - start_time)/1000
print(gap_time)