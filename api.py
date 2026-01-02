##for web requests
import requests

latitude=float(input("Enter the latitude:"))
longitude=float(input("Enter the longitude:"))
response=requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m")
data=response.json()
data.keys()
type(data.keys())
data.values()
data.items()
temperature=data["current"]["temperature_2m"]
print(temperature)