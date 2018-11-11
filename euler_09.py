finish = False
for a in range(2,1000):
    for b in range(1,a):
        if(1000*(a+b) - a*b)==500000:
            finish = True
            break
    if finish:
        break
print(a*b*(1000-a-b))