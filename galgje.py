import random


# ---------------- WOORDEN ----------------
def lees_woorden(bestandsnaam):
    with open(bestandsnaam, "r") as file:
        woorden = file.read().split("\n")

    woorden_dict = {}
    for woord in woorden:
        if woord == "":
            continue
        if len(woord) < 6:
            woorden_dict[woord] = 1
        elif len(woord) < 11:
            woorden_dict[woord] = 2
        else:
            woorden_dict[woord] = 3

    return woorden_dict


def sla_woorden_op(bestandsnaam, woorden_dict):
    with open(bestandsnaam, "w") as file:
        for woord in woorden_dict:
            file.write(woord + "\n")


# ---------------- SPEL ----------------
def bereken_score(levens, moeilijkheid):
    return levens * moeilijkheid


def voeg_score_toe(naam, woord, score):
    with open("scores.txt", "a") as file:
        file.write(f"{naam}|{woord}|{score}\n")


def toon_tussenstand(woord, geraden):
    resultaat = ""
    for letter in woord:
        if letter in geraden:
            resultaat += letter
        else:
            resultaat += "_"
        resultaat += " "
    return resultaat


def kies_woord(woorden, moeilijkheid):
    lijst = [w for w, m in woorden.items() if m == moeilijkheid]
    return random.choice(lijst)


def start_galgje():
    print("\n--- Start Galgje ---")

    moeilijkheid = input("Kies moeilijkheid (1, 2, 3): ")

    if moeilijkheid not in "123":
        print("Ongeldige keuze")
        return

    speel_sessie(int(moeilijkheid))


def speel_sessie(moeilijkheid):
    woorden = lees_woorden("words.txt")
    naam = input("Wat is je naam: ")

    levens = 10 if moeilijkheid == 1 else 8 if moeilijkheid == 2 else 6
    woord = kies_woord(woorden, moeilijkheid)
    geraden = []

    while levens > 0:
        stand = toon_tussenstand(woord, geraden)
        print(f"{stand} ({len(woord)} letters, {levens} levens)")

        if "_" not in stand:
            score = bereken_score(levens, moeilijkheid)
            print(f"Gewonnen! Score: {score}, bedankt voor het spelen {naam}!")
            voeg_score_toe(naam, woord, score)
            break

        letter = input("Raad een letter (enter = stop): ").lower()

        if letter == "":
            print(f"Het woord was: {woord}")
            break
        elif letter in geraden:
            print("Al geprobeerd")
        elif letter not in woord:
            print("Fout")
            levens -= 1
        else:
            print("Goed!")

        geraden.append(letter)

    print(f"Bedankt voor het spelen {naam}!")
    print(f"Het woord was: {woord}")


# ---------------- MENU ----------------
def galgje_menu():
    while True:
        print("\n--- GALGJE ---")
        print("1. Speel een sessie")
        print("2. Verwijder woord")
        print("3. Voeg woord toe")
        print("4. Toon aantal woorden")
        print("5. Terug")

        keuze = input("Keuze: ")

        if keuze == "1":
            start_galgje()

        elif keuze == "2":
            woorden = lees_woorden("words.txt")

            for w in woorden:
                print(w)

            woord = input("Welk woord verwijderen: ")

            if woord in woorden:
                del woorden[woord]
                sla_woorden_op("words.txt", woorden)
                print("Verwijderd")
            else:
                print("Bestaat niet")

        elif keuze == "3":
            woorden = lees_woorden("words.txt")

            woord = input("Welk woord toevoegen: ")

            if woord in woorden:
                print("Bestaat al")
                continue

            if not woord.isalpha():
                print("Ongeldig")
                continue

            if len(woord) < 6:
                woorden[woord] = 1
            elif len(woord) < 11:
                woorden[woord] = 2
            else:
                woorden[woord] = 3

            sla_woorden_op("words.txt", woorden)
            print("Toegevoegd")

        elif keuze == "4":
            woorden = lees_woorden("words.txt")
            print(f"Aantal woorden: {len(woorden)}")

        elif keuze == "5":
            break

        else:
            print("Ongeldige keuze")