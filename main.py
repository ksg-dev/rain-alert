import requests

api_key = "856b43ff1555aead490c92cbf0d86355"
MY_LAT = 30.673290
MY_LONG = -88.111153

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
}

# url: https://api.openweathermap.org/data/2.5/forecast?lat=30.673290&lon=-88.111153&appid=856b43ff1555aead490c92cbf0d86355

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()

weather_id = data["list"][0]["weather"][0]["id"]
weather_desc = data["list"][0]["weather"][0]["description"]

print(weather_id)
print(weather_desc)

# print(data)