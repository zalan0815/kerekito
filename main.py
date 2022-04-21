import math

f = "igen"

while f == "igen": 

    sz = float(input("Kerekítendő szám:"))

    def kerek(sz):
        if sz - math.floor(sz) < 0.5:
            n = math.floor(sz)
            print(n)
        elif sz - math.floor(sz) >= 0.5:
            n = math.ceil(sz)
            print(n)
        else:
            print('Hiba történt')

    kerek(sz)

    f = input('Folytatni szeretnéd? (igen/nem)')

if f == "nem":
    print("Viszlát!")
