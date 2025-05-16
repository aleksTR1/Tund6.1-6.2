import random

sonastik = {
    'koer': 'собака',
    'kass': 'кошка',
    'maja': 'дом',
    'auto': 'машина',
    'päike': 'солнце'
}

def tolgi_est_rus(sona):
    return sonastik.get(sona.lower(), "Sõna puudub")

def tolgi_rus_est(sona):
    for est, rus in sonastik.items():
        if rus == sona.lower():
            return est
    return "Sõna puudub"

def lisa_sona():
    est = input("Eesti sõna: ").lower()
    rus = input("Vene tõlge: ").lower()
    sonastik[est] = rus
    print("Sõna lisatud!")

def paranda_sona():
    est = input("Paranda sõna (eesti): ").lower()
    if est in sonastik:
        uus = input("Uus vene tõlge: ").lower()
        sonastik[est] = uus
        print("Parandus tehtud!")
    else:
        print("Sõna pole sõnastikus")

def testi_teadmisi():
    keys = list(sonastik.keys())
    correct = 0
    for i in range(3):
        est = random.choice(keys)
        vastus = input(f"Vene tõlge sõnale '{est}': ").lower()
        if vastus == sonastik[est]:
            print("Õige!")
            correct += 1
        else:
            print(f"Vale! Õige vastus: {sonastik[est]}")
    protsent = (correct / 3) * 100
    print(f"Tulemus: {protsent:.0f}%")

while True:
    print("\nValikud:")
    print("1 - Eesti -> Vene")
    print("2 - Vene -> Eesti")
    print("3 - Lisa sõna")
    print("4 - Paranda sõna")
    print("5 - Testi teadmisi")
    print("6 - Välju")
    valik = input("Tee valik: ")

    if valik == '1':
        s = input("Eesti sõna: ")
        print("Tõlge:", tolgi_est_rus(s))
    elif valik == '2':
        s = input("Vene sõna: ")
        print("Tõlge:", tolgi_rus_est(s))
    elif valik == '3':
        lisa_sona()
    elif valik == '4':
        paranda_sona()
    elif valik == '5':
        testi_teadmisi()
    elif valik == '6':
        print("Head aega!")
        break
    else:
        print("Vale valik!")
