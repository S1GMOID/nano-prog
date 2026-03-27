import random

def genereer_getal(moeilijkheid):
    if moeilijkheid == 1:
        return random.randint(1, 10)
    elif moeilijkheid == 2:
        return random.randint(1, 50)
    else:
        return random.randint(1, 100)

def max_pogingen(moeilijkheid):
    if moeilijkheid == 1:
        return 5
    elif moeilijkheid == 2:
        return 7
    else:
        return 10

def bereken_score(moeilijkheid, gebruikte_pogingen, max_pogingen):
    return (max_pogingen - gebruikte_pogingen) * moeilijkheid

def advies_moeilijkheidsgraad(score):
    if score < 5:
        return "Probeer een lagere moeilijkheidsgraad"
    elif score <= 12:
        return "Houd deze moeilijkheidsgraad aan"
    else:
        return "Je kunt een hogere moeilijkheidsgraad aan!"

def raad_het_nummer():
    naam = input("Wat is je naam? ")

    if naam == "":
        print("Geen naam ingevoerd")
        return

    print("Kies moeilijkheidsgraad: 1=makkelijk, 2=normaal, 3=moeilijk")
    invoer = input("Jouw keuze: ")

    if invoer not in ["1", "2", "3"]:
        print("Foute invoer")
        return

    moeilijkheid = int(invoer)
    te_raden_getal = genereer_getal(moeilijkheid)
    max_pog = max_pogingen(moeilijkheid)

    gevonden = False

    for poging in range(1, max_pog + 1):
        gok_input = input("Doe een gok: ")

        if not gok_input.isdigit():
            print("Foute invoer")
            continue   # 🔥 FIX: niet stoppen maar opnieuw vragen

        gok = int(gok_input)

        if gok == te_raden_getal:
            print("Gevonden!")
            gevonden = True
            gebruikte_pogingen = poging
            break

        elif gok < te_raden_getal:
            if te_raden_getal - gok <= 2:
                print("Dichtbij! Hoger!")
            else:
                print("Hoger!")

        else:
            if gok - te_raden_getal <= 2:
                print("Dichtbij! Lager!")
            else:
                print("Lager!")

        print("Nog pogingen:", max_pog - poging)
        print("Huidige score:", (max_pog - poging) * moeilijkheid)

    if not gevonden:
        print("Helaas, niet geraden. Het getal was:", te_raden_getal)
        gebruikte_pogingen = max_pog

    score = bereken_score(moeilijkheid, gebruikte_pogingen, max_pog)

    print("Eindscore:", score)
    print("Advies:", advies_moeilijkheidsgraad(score))