import requests

def toon_weer():
    print("\n+-+ Weer App +-+")

    stad = input("Kies een stad (amsterdam/rotterdam/utrecht): ").lower()

    if stad == "amsterdam":
        lat = 52.37
        lon = 4.89
    elif stad == "rotterdam":
        lat = 51.92
        lon = 4.48
    elif stad == "utrecht": #mn stadsie
        lat = 52.09
        lon = 5.12
    else:
        print("Stad niet gevonden!")
        return

    url = "https://api.open-meteo.com/v1/forecast?latitude=" + str(lat) + "&longitude=" + str(lon) + "&current_weather=true" #raak dit alsjeblieft niet aan

    try:
        response = requests.get(url)
        data = response.json()

        temperatuur = data["current_weather"]["temperature"]
        wind = data["current_weather"]["windspeed"]

        print("\nWeer in " + stad + ":")
        print("Temperatuur: " + str(temperatuur) + "°C")
        print("Wind: " + str(wind) + " km/u")

    except:
        print("Kon geen weerdata ophalen!")

