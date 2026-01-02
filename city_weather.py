import requests
def get_weather(place):
    latitude, longitude= get_lat_long(place)
    response=requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m")
    data=response.json()
    #print(data)
    return data["current"]["temperature_2m"]

def get_lat_long(place):
    url=f"https://geocoding-api.open-meteo.com/v1/search?name={place}"
    response=requests.get(url)
    result=response.json()

    if "results" not in result or len(result["results"]) == 0:
        raise ValueError("City not found. Please check spelling.")
    
    lat=result["results"][0]["latitude"]
    lon=result["results"][0]["longitude"]
    return lat, lon

n=1
while n!=0:
    city=input("Enter the city name:")
    result=get_weather(place=city)
    print(f"The current temperature of {city} is: {result}°C")
    n=int(input("To Continue press 1 else press 0: "))