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
        

print ("##############")


 
 
auto = ["ferrari", "Honda", "porsche", "Alfa Romeo", "BMW"]
moto = ["KTM", "Yamaha", "Kawasaki", "Ducati"]
listona =  auto +  moto

listona.sort()
print(listona)


print ("##############")



numeri = []
for i in range(50):
    numeri.append(random.randint(0, 1000))
    numeri_dispari = []
for x in numeri:
    if x%2 == 1:
        numeri_dispari.append(x)
    numeri = numeri_dispari
print(numeri)


