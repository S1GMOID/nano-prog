# main.py

from galgje import speel_sessie
from raadtnummer import raad_het_nummer
from weatherapi import toon_weer


def main():
    while True:
        print("\n-+- Nano App Store -+-")
        print("1. Hangman")
        print("2. Raad het nummer")
        print("3. Weer")
        print("4. Stop")

        keuze = input("Maak een keuze: ")

        import galgje

        if keuze == "1":
            galgje.galgje_menu() #voor sprint2
        elif keuze == "2":
            print("\n--- Raad het nummer ---")
            raad_het_nummer()  #voor sprint1
        elif keuze == "3":
            toon_weer()  #voor de api
        elif keuze == "4":
            print("Fijne dag nog!")
            break
        else:
            print("Ongeldig! Kies een optie tussen 1-4.")

if __name__ == "__main__":
    main()