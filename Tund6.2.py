sonad = [
    {'est': 'koer', 'rus': 'собака', 'eng': 'dog'},
    {'est': 'kass', 'rus': 'кошка', 'eng': 'cat'},
    {'est': 'maja', 'rus': 'дом', 'eng': 'house'},
    {'est': 'auto', 'rus': 'машина', 'eng': 'car'},
    {'est': 'päike', 'rus': 'солнце', 'eng': 'sun'}
]

# Переводчик
def tolkija(sonad, allikas, siht, sona):
    for kirje in sonad:
        if kirje[allikas] == sona.lower():
            return kirje[siht]
    return "Sõna ei leitud!"

# Добавление слова
def lisa_sona(sonad):
    print("Lisame uue sõna:")
    uus_est = input("Sisesta eesti keeles: ").strip().lower()
    uus_rus = input("Sisesta vene keeles: ").strip().lower()
    uus_eng = input("Sisesta inglise keeles: ").strip().lower()
    sonad.append({'est': uus_est, 'rus': uus_rus, 'eng': uus_eng})
    print("Sõna lisatud!")

# Исправление слова
def paranda_sona(sonad):
    vana_sona = input("Sisesta sõna, mida parandada (ükskõik mis keel): ").strip().lower()
    for kirje in sonad:
        if vana_sona in kirje.values():
            print("Leitud:", kirje)
            kirje['est'] = input("Uus eesti sõna: ").strip().lower()
            kirje['rus'] = input("Uus vene sõna: ").strip().lower()
            kirje['eng'] = input("Uus inglise sõna: ").strip().lower()
            print("Sõna parandatud!")
            return
    print("Sõna ei leitud!")

# Тест
import random
def testi_teadmisi(sonad):
    print("Test algab! 5 küsimust.")
    allikad = ['est', 'rus', 'eng']
    punktid = 0
    for _ in range(5):
        suund = random.choice([(a, b) for a in allikad for b in allikad if a != b])
        valik = random.choice(sonad)
        print(f"Tõlgi sõna '{valik[suund[0]]}' keelest {suund[0]} → {suund[1]}")
        vastus = input("Sinu vastus: ").strip().lower()
        if vastus == valik[suund[1]]:
            print("Õige!")
            punktid += 1
        else:
            print(f"Vale! Õige vastus on: {valik[suund[1]]}")
    print(f"Said {punktid} punkti 5st.")

# Главное меню
def menuu():
    while True:
        print("\n=== Sõnastik ===")
        print("1 - Tõlgi sõna")
        print("2 - Lisa uus sõna")
        print("3 - Paranda sõna")
        print("4 - Teadmiste test")
        print("5 - Välju")
        valik = input("Vali tegevus: ")

        if valik == '1':
            allikas = input("Millisest keelest? (est/rus/eng): ").strip().lower()
            siht = input("Millisesse keelde? (est/rus/eng): ").strip().lower()
            sona = input("Sisesta sõna: ").strip().lower()
            print("Tõlge:", tolkija(sonad, allikas, siht, sona))
        elif valik == '2':
            lisa_sona(sonad)
        elif valik == '3':
            paranda_sona(sonad)
        elif valik == '4':
            testi_teadmisi(sonad)
        elif valik == '5':
            print("Head aega!")
            break
        else:
            print("Vale valik!")

if __name__ == "__main__":
    menuu()
