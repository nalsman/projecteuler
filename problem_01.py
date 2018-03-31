sum = 0;
for index in range(1000):
    if(index % 3 == 0):
        sum += index
    else:
        if(index % 5 == 0):
            sum += index
print(sum)
