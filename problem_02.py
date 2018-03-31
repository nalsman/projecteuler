# Fibonanci sum of even-valued term when highest value is lower than 4mil
prev01 = 0
prev02 = 1
current = 0
sum = 0
while current < 4000000:
    current = prev01 + prev02
    if current > 4000000:
        break;
    print("Prev01: ", prev01, "Prev02: ", prev02, "Current: ", current)
    prev01 = prev02
    prev02 = current
    if current % 2 == 0:
        sum += current
print("Total of even-valued: ",sum)