sumA = 0
sumB = 0
for i in range(1,101):
    sumA += (i**2)
    sumB += i
print(sumA - sumB**2)