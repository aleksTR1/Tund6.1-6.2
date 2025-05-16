import random
import pyttsx3

# Исходные данные — список словарей
sonad = [
    {'est': 'koer', 'rus': 'собака', 'eng': 'dog'},
    {'est': 'kass', 'rus': 'кошка', 'eng': 'cat'},
    {'est': 'maja', 'rus': 'дом', 'eng': 'house'},
    {'est': 'auto', 'rus': 'машина', 'eng': 'car'},
    {'est': 'päike', 'rus': 'солнце', 'eng': 'sun'}
]

def tolkija(sonad, allikas, siht, sona):
    for kirje in sonad:
        if kirje[allikas] == sona.lower():
            return kirje[siht]
    return "Sõna ei leitud!"

def lisa_sona(sonad):
    est = input("Eesti: ").strip().lower()
    rus = input("Vene: ").strip().lower()
    eng = input("Inglise: ").strip().lower()
    sonad.append({'est': est, 'rus': rus, 'eng': eng})
    print("Sõna lisatud!")

def paranda_sona(sonad):
    keele_valik = input("Paranda sõna keeles (est/rus/eng): ").strip().lower()
    vana = input("Sisesta vana sõna: ").strip().lower()
    uus = input("Sisesta uus sõna: ").strip().lower()
    for kirje in sonad:
        if kirje[keele_valik] == vana:
            kirje[keele_valik] = uus
            print("Parandus tehtud!")
            return
    print("Sõna ei leitud.")

def testi_teadmisi(sonad):
    keeled = ['est', 'rus', 'eng']
    õige = 0
    küsimuste_arv = 3
    for _ in range(küsimuste_arv):
        kirje = random.choice(sonad)
        allikas = random.choice(keeled)
        siht = random.choice([k for k in keeled if k != allikas])
        vastus = input(f"Tõlgi '{kirje[allikas]}' keelest {allikas} keelde {siht}: ").strip().lower()
        if vastus == kirje[siht]:
            print("Õige!")
            õige += 1
        else:
            print(f"Vale! Õige vastus on '{kirje[siht]}'")
    protsent = õige / küsimuste_arv * 100
    print(f"Tulemus: {protsent:.0f}%")

def text_to_speech(sona, keel='eng'):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # Пример: русская озвучка — voices[1], английская — voices[0], эстонская может отсутствовать
    if keel == 'rus':
        engine.setProperty('voice', voices[1].id)
    else:
        engine.setProperty('voice', voices[0].id)
    engine.say(sona)
    engine.runAndWait()

def kuva_menuu():
    print("\nValikud:")
    print("1 - Tõlgi")
    print("2 - Lisa sõna")
    print("3 - Paranda sõna")
    print("4 - Testi teadmisi")
    print("5 - Kuula sõna")
    print("6 - Välju")

def vali_keel(prompt):
    valik = input(prompt).strip().lower()
    if valik in ['est', 'rus', 'eng']:
        return valik
    else:
        print("Vale keel, proovi uuesti.")
        return vali_keel(prompt)

def main():
    print("Tere tulemast kolme keele sõnastikku!")
    while True:
        kuva_menuu()
        valik = input("Tee valik: ").strip()
        if valik == '1':
            allikas = vali_keel("Sisesta algkeel (est/rus/eng): ")
            siht = vali_keel("Sisesta sihtkeel (est/rus/eng): ")
            sona = input("Sisesta sõna: ").strip().lower()
            print("Tõlge:", tolkija(sonad, allikas, siht, sona))
        elif valik == '2':
            lisa_sona(sonad)
        elif valik == '3':
            paranda_sona(sonad)
        elif valik == '4':
            testi_teadmisi(sonad)
        elif valik == '5':
            keel = vali_keel("Sisesta keele kood, et kuulata sõna (est/rus/eng): ")
            sona = input("Sisesta sõna, mida kuulata: ").strip()
            text_to_speech(sona, keel)
        elif valik == '6':
            print("Head aega!")
            break
        else:
            print("Vale valik!")

if __name__ == "__main__":
    main()
