inputfile = open('./grid.txt')
lines = inputfile.readlines()
data = list()

for line in lines:
    elements = line.split()
    elements = [int(ele) for ele in elements]
    data.append(elements)

max_prod = 0
for x in range(0,17):
    for y in range(0,17):
        product = data[x][y]*data[x+1][y+1]*data[x+2][y+2]*data[x+3][y+3]
        if product > max_prod:
                max_prod = product
for x in range(0,20):
    for y in range(0,17):
        product = data[x][y]*data[x][y+1]*data[x][y+2]*data[x][y+3]
        if product > max_prod:
                max_prod = product
for x in range(0,17):
    for y in range(0,20):
        product = data[x][y]*data[x+1][y]*data[x+2][y]*data[x+3][y]
        if product > max_prod:
                max_prod = product
for x in range(3,20):
    for y in range(0,17):
        product = data[x][y]*data[x-1][y+1]*data[x-2][y+2]*data[x-3][y+3]
        if product > max_prod:
                max_prod = product
print(max_prod)