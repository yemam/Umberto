# Esercizio I 
Animali = ["cane", "gatto", "pescespada", "kanguro", "civetta"]
Numeri = [6, 3, 45, 1, 756, 2]
Lista_grande = Animali + Numeri

for x in Lista_grande:
   if isinstance(x, int) and x > 5:
    print(x)


