# raad het nummer spelletje
import random


def main():

    print("Welkom bij het raad het nummer spelletje!")
    print("Ik heb een nummer tussen 1 en 100 gekozen. Kun jij het raden?")
    
    nummer = random.randint(1, 100)
    geraden = False
    
    while not geraden:
        try:
            gok = int(input("Voer je gok in: "))
            if gok < nummer:
                print("Te laag! Probeer het opnieuw.")
            elif gok > nummer:
                print("Te hoog! Probeer het opnieuw.")
            else:
                print("Gefeliciteerd! Je hebt het nummer geraden!")
                geraden = True
        except ValueError:
            print("Ongeldige invoer. Voer alstublieft een getal in.")