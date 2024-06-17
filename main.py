import requests

OWM_EndPoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "856b43ff1555aead490c92cbf0d86355"
MY_LAT = 30.673290
MY_LONG = -88.111153

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}

# url: https://api.openweathermap.org/data/2.5/forecast?lat=30.673290&lon=-88.111153&appid=856b43ff1555aead490c92cbf0d86355&cnt=4

response = requests.get(url=OWM_EndPoint, params=parameters)
response.raise_for_status()
data = response.json()

weather_codes = [data["list"][i]["weather"][0]["id"] for i in range(0,4)]
weather_id = data["list"][0]["weather"][0]["id"]
weather_desc = data["list"][0]["weather"][0]["description"]

# print(weather_id)
# print(weather_desc)

print(f"weather codes: {weather_codes}")

will_rain = False
for code in weather_codes:
    if code < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")

# print(data)
