import requests
from twilio.rest import Client

API_KEY = "b239ad6816f4e09d41069588e7ac2d80"
account_sid = "Your_sid"
auth_token = "Your_auth_token"

parameters = {
    "lat": "Yourlat",
    "lon": "Yourlong",
    "appid": API_KEY,
    "exclude": "daily,minutely,current"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly_weather = weather_data["hourly"]
hours_code = [data["weather"][0]["id"] for data in hourly_weather]
final_hours = hours_code[:12]
rain = False
for data in final_hours:
    if data < 600:
        rain = True
        break
if rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to carry an ☂",
        from_="twilionum",
        to="yournum"
    )
    print(message.status)