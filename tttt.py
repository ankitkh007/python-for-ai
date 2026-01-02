import requests

def get_coordinates(place):
    url = f"http://api.positionstack.com/v1/forward?access_key=72f2eb0b0f9c97eb1029c56184bc29fc&query={place}"
    r = requests.get(url)
    result = r.json()

    print("\n----------- RAW POSITIONSTACK RESPONSE -----------")
    print(result)
    print("--------------------------------------------------\n")

    # Case 1 -> Normal PositionStack response
    if "data" in result and len(result["data"]) > 0:
        lat = result["data"][0]["latitude"]
        lon = result["data"][0]["longitude"]
        return lat, lon

    # Case 2 -> Some users get flat JSON
    elif "latitude" in result and "longitude" in result:
        return result["latitude"], result["longitude"]

    else:
        raise ValueError("PositionStack did NOT return coordinates!")

def get_weather(place):
    lat, lon = get_coordinates(place)

    r = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m"
    )
    data = r.json()

    return data["current"]["temperature_2m"]


while True:
    city = input("Enter city: ")
    print("Temp =", get_weather(city))
