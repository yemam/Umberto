import random
x = random.randint(0,50)
y = random.randint(0,50)
z = random.randint(0,50)

if x < y and x < z:
    print(x)
    if y < z:
        print(y)
        print(z)
    else:
        print(z)
        print(y)


elif y < z:
    print(y)
    if x < z:
        print(x)
        print(z)
    else: 
        print(z)
        print(x)

else:
    print(z)

    if x < y:
        print(x)
        print(z)

    else:
        print(y)
        print(x)
        



